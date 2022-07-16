from sklearn.datasets import load_iris


if __name__ == "__main__":
    iris = load_iris()
    X = iris.data[:, :]  
    y = iris.target

    print("X.shape", X.shape)
    print("y.shape", y.shape)
    print(X[0], y[0])