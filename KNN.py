import numpy as np
import math

class KNN:
    def __init__(self, X_train, y_train):
        self.X_train = X
        self.y_train = y 

    def predict(self, X_test):
        distances = self._get_distances(X_test)

    def _get_distances(self, X_test):
        [(x) for x in X_test]

    def _calc_distance(self, x_1, x_2):
        d = 0
        for index, i in x_1:
            d += (i - x_2) ** 2

        return math.sqrt(d)



