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
        self.classes_ = np.sort(np.unique(y))
        self.__set_classifiers()
        X_splitted = self.__split_dataset(X)

        # fitting each ensemble
        for s_index in range(self.s):
            for k_index in range(len(self.k)):
                self.classifiers[s_index][k_index].fit(X_splitted[s_index],
                                                       y)

        return self

    # this method performing the interval thresholding
    def predict(self, X):
        predictions = self.predict_proba(X)
        result = []
        for aggregation in predictions:
            if self.t < aggregation[0]:  # down(u) > t
                result.append(1)  # main class
            elif aggregation[1] < self.t:  # up(u) < t
                result.append(0)  # subordinate class
            else:
                result.append(-1)  # not belong to any class
        return np.array(result)

    def predict_proba(self, X):
        X_splitted = self.__split_dataset(X)
        intervals = np.empty((len(X), self.s,
                              2))
        for s_index in range(self.s):  # for each subtable (s)
            predictions = np.empty(
                (len(X), len(self.k)))
            for k_index in range(len(self.k)): # for each k in R
                classifier = self.classifiers[s_index][k_index]
                prediction = classifier.predict_proba(X_splitted[s_index])[:, 1]  # getting the main class confidence
                predictions[:, k_index] = prediction
            interval = np.column_stack((predictions.min(axis=1), predictions.max(
                axis=1)))  # creating intervals
            intervals[:, s_index] = interval
        predictions = self.__get_predictions(intervals)  # aggregation of intervals from each subtable

        return predictions

    def score(self, X, y, sample_weight=None):
        return self.score_acc(X, y, sample_weight)

    def score_acc(self, X, y, sample_weight=None):
        predictions = self.predict(X)
        score_acc = self.__score__acc(y, predictions, X)
        score_coverage = self.__score_coverage(predictions)
        score_u_area = self.__score_u_area(predictions)

        return score_acc, score_coverage, score_u_area

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
            aggregation = self.aggregation.aggregate_numpy_arrays_representation(interval)
            result.append(aggregation)
        return np.array(result)

    def __score__acc(self, y, predictions, X):
        predictions_array = np.array(predictions)
        filter_indices = np.where(
            predictions_array != -1)  # selecting not labelled instances
        y_filtered = y[filter_indices]
        predictions_filtered = predictions_array[
            filter_indices]
        return metrics.accuracy_score(y_filtered, predictions_filtered)

    def __score_coverage(self, predictions):
        return 1 - self.__score_u_area(predictions)

    def __score_u_area(self, predictions):
        predictions = predictions.tolist()
        return predictions.count(-1) / len(predictions)
