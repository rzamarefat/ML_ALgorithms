import numpy as np


class LinearRegression:
    def __init__(self, num_iteration=1000, lr=0.001):
        self.num_iteration=num_iteration
        self.lr = lr

    def train(self, X_train, y_train):
        num_samples, num_features = X_train.shape

        self.weights = np.zeros(num_features)
        self.bias = 0
        

        for _ in range(self.num_iteration):
            y_predicted = np.dot(X_train, self.weights) + self.bias

            dw = (1 / num_samples) * np.dot(X_train.T, (y_predicted - y_train))
            db = (1 / num_samples) * np.sum(y_predicted - y_train)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
