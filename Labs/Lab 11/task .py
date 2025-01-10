import numpy as np
def calculate_entropy(data, target_col):
    target_values = data[:, target_col]
    unique, counts = np.unique(target_values, return_counts=True)
    probabilities = counts / counts.sum()
    return -np.sum(probabilities * np.log2(probabilities))

def calculate_information_gain(data, attribute_col, target_col):
    total_entropy = calculate_entropy(data, target_col)
    attribute_values = data[:, attribute_col]
    unique, counts = np.unique(attribute_values, return_counts=True)
    weighted_entropy = 0
    for value, count in zip(unique, counts):
        subset = data[attribute_values == value]
        weighted_entropy += (count / len(data)) * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy

def build_tree(data, attributes, target_col):
    target_values = data[:, target_col]
    if len(np.unique(target_values)) == 1:
        return target_values[0]
    if len(attributes) == 0:
        unique, counts = np.unique(target_values, return_counts=True)
        return unique[np.argmax(counts)]
    gains = [calculate_information_gain(data, attr, target_col) for attr in attributes]
    best_attribute = attributes[np.argmax(gains)]
    tree = {best_attribute: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attribute]
    unique_values = np.unique(data[:, best_attribute])
    for value in unique_values:
        subset = data[data[:, best_attribute] == value]
        if len(subset) == 0:
            unique, counts = np.unique(target_values, return_counts=True)
            tree[best_attribute][value] = unique[np.argmax(counts)]
        else:
            tree[best_attribute][value] = build_tree(subset, remaining_attributes, target_col)
    return tree
def predict(tree, data_point, attribute_names):
    if not isinstance(tree, dict):
        return tree
    root_node = next(iter(tree))
    value = data_point[attribute_names[root_node]]
    subtree = tree[root_node].get(value, "Unknown")
    return predict(subtree, data_point, attribute_names) if isinstance(subtree, dict) else subtree

if __name__ == "__main__":
    dataset = pd.read_csv('Employee.csv')
    attribute_names = dataset.columns
    dataset = dataset.to_dict(orient="records")
    # print(dataset)
    data = []
    for i in range(len(dataset)):
        data.append(list(dataset[i].values()))
    data = np.array(data)
    attributes = [0, 1 ,2 ,3,4,5,6,7]
    target_col = 8
    # print(data)
    # print(dataset)
    # print(attribute_names)
    dictionary = {}
    for i in range(len(attribute_names)):
        dictionary[i] = attribute_names[i]
    decision_tree = build_tree(data, attributes, target_col)
    print("Decision Tree:")

    print(decision_tree)

    test_data = {'Education':"Bachelors",'JoiningYear': 2017,'City': "Bangalore",'PaymentTier':3,'Age':34,'Gender':'Male','EverBenched':"No",'ExperienceInCurrentDomain':0}

    # prediction = predict(decision_tree, test_data, dictionary)
    # print("\nPrediction for test data:", prediction)