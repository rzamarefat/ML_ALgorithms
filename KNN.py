import numpy as np
import math

class KNN:
    def __init__(self, X_train, y_train, k=3):
        self.X_train = X_train
        self.y_train = y_train
        self.k = k

    def train(self, sample):
        distances = [(self._calc_distance(sample, x), y) for x, y in zip(self.X_train, self.y_train)]
        distances.sort(key=lambda a: a[0])

        classes_holder = [class_ for (_, class_) in distances[0: self.k]]
        predicted_class = max(set(classes_holder), key = classes_holder.count)

        print(f"The sample belongs to the class: {predicted_class}")
        

    def _calc_distance(self, sample_1, sample_2):
        return np.sqrt(np.sum((sample_1 - sample_2) ** 2))