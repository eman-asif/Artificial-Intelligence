import numpy as np
import matplotlib.pyplot as plt

def perceptron(X, y, learning_rate=0.01, epochs=100):
    weights = np.zeros(X.shape[1])
    bias = 0
    for _ in range(epochs):
        for i in range(len(X)):
            linear_output = np.dot(X[i], weights) + bias
            prediction = 1 if linear_output > 0 else 0
            update = learning_rate * (y[i] - prediction)
            weights += update * X[i]
            bias += update
    
    return weights, bias

def plot_perceptron_boundary(X, y, weights, bias):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = np.dot(np.c_[xx.ravel(), yy.ravel()], weights) + bias
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z > 0, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
    plt.show()
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  

weights , bias = perceptron(X, y)
plot_perceptron_boundary(X, y, weights, bias)

import tensorflow as tf
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

def train_xor_nn(X, y):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(4, input_dim=2, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=100, verbose=0)
    return model

def visualize_xor_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z > 0.5, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
    plt.show()

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

model = train_xor_nn(X, y)
visualize_xor_boundary(model, X, y)