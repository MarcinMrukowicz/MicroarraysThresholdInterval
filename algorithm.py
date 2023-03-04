import numpy as np
from sklearn import metrics
from sklearn.base import ClassifierMixin, BaseEstimator
from sklearn.neighbors import KNeighborsClassifier


class Algorithm(BaseEstimator, ClassifierMixin):
    def __init__(self, s, k, t, aggregation, random_state, n_jobs):
        self.s = s
        self.k = k
        self.t = t
        self.aggregation = aggregation
        self.random_state = random_state
        self.n_jobs = n_jobs

    def fit(self, X, y=None):
        self.__set_classifiers()
        X_splitted = self.__split_dataset(X)

        for s_index in range(self.s):
            for k_index in range(len(self.k)):
                self.classifiers[s_index][k_index].fit(X_splitted[s_index], y)

        return self

    def predict(self, X):
        X_splitted = self.__split_dataset(X)
        intervals = np.empty((len(X), self.s, 2))
        for s_index in range(self.s):
            predictions = np.empty((len(X), len(self.k)))
            for k_index in range(len(self.k)):
                classifier = self.classifiers[s_index][k_index]
                prediction = classifier.predict(X_splitted[s_index])
                predictions[:, k_index] = prediction
            interval = np.column_stack((predictions.min(axis=1), predictions.max(axis=1)))
            intervals[:, s_index] = interval
        predictions = self.__get_predictions(intervals)

        return predictions

    def score(self, X, y, sample_weight=None):
        predictions = self.predict(X)
        score_auc = self.__score_auc(y, predictions)
        score_coverage = self.__score_coverage(predictions)
        score_u_area = self.__score_u_area(predictions)

        print('scores:', score_auc, score_coverage, score_u_area)
        return score_auc

    def __set_classifiers(self):
        self.classifiers = [
            [KNeighborsClassifier(n_neighbors=self.k[k_index], n_jobs=self.n_jobs) for k_index in range(len(self.k))]
            for _ in range(self.s)
        ]

    def __split_dataset(self, X):
        return np.array_split(X, self.s, axis=1)

    def __get_predictions(self, intervals):
        result = []
        for interval in intervals:
            aggregation = self.aggregation(interval)
            if  aggregation[0] > self.t:
                result.append(1)
            elif aggregation[0] < self.t:
                result.append(0)
            else:
                result.append(None)
        return result

    def __score_auc(self, y, predictions):
        predictions_array = np.array(predictions)
        filter_indices = np.where(predictions_array != None)
        y_filtered = y[filter_indices].tolist()
        predictions_filtered = predictions_array[filter_indices].tolist()
        fpr, tpr, thresholds = metrics.roc_curve(y_filtered, predictions_filtered)
        return metrics.auc(fpr, tpr)

    def __score_coverage(self, predictions):
        return 1 - self.__score_u_area(predictions)

    def __score_u_area(self, predictions):
        return predictions.count(None) / len(predictions)
