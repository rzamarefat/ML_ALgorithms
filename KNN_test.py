from sklearn.datasets import load_iris
from KNN import KNN
import numpy as np

if __name__ == "__main__":
    iris = load_iris()
    X = iris.data[:, :]  
    y = iris.target

    knn = KNN(X_train=X, y_train=y)
    
    test_sample = np.array([5.1, 3.5, 1.4, 0.2])
    knn.train(test_sample)