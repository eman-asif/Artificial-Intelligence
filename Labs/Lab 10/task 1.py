import math
from collections import Counter
import random

def calculate_entropy(data, target_col):
    counts = Counter(row[target_col] for row in data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    values = set(row[attribute] for row in data)
    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / len(data)) * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy

def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if depth == max_depth or all(row[target_col] == data[0][target_col] for row in data):
        return Counter(row[target_col] for row in data).most_common(1)[0][0]
    best_attr = max(attributes, key=lambda attr: calculate_information_gain(data, attr, target_col))
    tree = {best_attr: {}}
    values = set(row[best_attr] for row in data)
    for value in values:
        subset = [row for row in data if row[best_attr] == value]
        tree[best_attr][value] = build_tree(subset, [attr for attr in attributes if attr != best_attr], target_col, depth + 1, max_depth)
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    attr = next(iter(tree))
    return predict(tree[attr][data_point[attr]], data_point)

def build_random_forest(data, attributes, target_col, n_trees=2, max_depth=3):
    forest = []
    for _ in range(n_trees):
        subset = random.choices(data, k=len(data))
        tree = build_tree(subset, attributes, target_col, max_depth=max_depth)
        forest.append(tree)
    return forest

def predict_forest(forest, data_point):
    predictions = [predict(tree, data_point) for tree in forest]
    return Counter(predictions).most_common(1)[0][0]

data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Hot', 'Play?': 'No'},
]

attributes = ['Weather', 'Temperature']
target_col = 'Play?'

forest = build_random_forest(data, attributes, target_col, n_trees=2, max_depth=3)
test_data = {'Weather': 'Sunny', 'Temperature': 'Hot'}
print("Prediction:", predict_forest(forest, test_data))