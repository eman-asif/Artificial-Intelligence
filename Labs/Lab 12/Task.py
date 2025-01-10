import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cross_entropy_loss(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-10, 1 - 1e-10)
    return -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def gradient_descent(X, y, weights, learning_rate, iterations):
    # m = len(y)
    for i in range(iterations):
        z = np.dot(X, weights)
        predictions = sigmoid(z)
        gradient = np.dot(X.T, (predictions - y)) 
        weights -= learning_rate * gradient
        if i % 100 == 0:
            loss = cross_entropy_loss(y, predictions)
            print(f"Iteration {i}, Loss: {loss:.4f}")
    return weights

def predict(X, weights):
    return sigmoid(np.dot(X, weights)) >= 0.5

def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    weights = np.zeros(X.shape[1])
    weights = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights

def evaluate(y_true, y_pred):
    return np.mean(y_true == y_pred)

if __name__ == "__main__":
    data = np.array([
        [0.1, 1.1, 0],
        [1.2, 0.9, 0],
        [1.5, 1.6, 1],
        [2.0, 1.8, 1],
        [2.5, 2.1, 1],
        [0.5, 1.5, 0],
        [1.8, 2.3, 1],
        [0.2, 0.7, 0],
        [1.9, 1.4, 1],
        [0.8, 0.6, 0]
    ])
    # y = t + tx
    # y = t + t1x + t2x
    X = data[:, :-1]
    y = data[:, -1]
    
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    # print(X)
    X = np.hstack((np.ones((X.shape[0], 1)), X))
    learning_rate = 0.01
    iterations = 1000
    weights = logistic_regression(X, y, learning_rate, iterations)
    y_pred = predict(X, weights)
    accuracy = evaluate(y, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 1][y == 0], X[:, 2][y == 0], label="Class 0", color="red")
    plt.scatter(X[:, 1][y == 1], X[:, 2][y == 1], label="Class 1", color="blue")
    x1 = np.linspace(-2, 2, 100)
    x2 = -(weights[0] + weights[1] * x1) / weights[2]
    plt.plot(x1, x2, label="Decision Boundary", color="green")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.title("Logistic Regression Decision Boundary")
    plt.show()