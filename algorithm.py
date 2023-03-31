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
        X_splitted = self.__split_dataset(X)  # podział na podzbiory

        for s_index in range(self.s):
            for k_index in range(len(self.k)):
                self.classifiers[s_index][k_index].fit(X_splitted[s_index],
                                                       y)  # uczenie klasyfikatora dla poszczególnego podzbioru i k

        return self

    # metoda predict oblicza "ostre" labele, wykonując progowanie
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

    # tutaj zostaje
    def predict_proba(self, X):
        X_splitted = self.__split_dataset(X)  # podział na podzbiory
        intervals = np.empty((len(X), self.s,
                              2))  # inicjalizacja tablicy na przedziały wymiary (ilość obiektów w zbiorze / s / 2 - [down, up])
        for s_index in range(self.s):  # dla każdego s
            predictions = np.empty(
                (len(X), len(self.k)))  # inicjalizacja tablicy na predykcje dla każdego elementu z podzbioru s
            for k_index in range(len(self.k)):  # dla każdego k
                classifier = self.classifiers[s_index][k_index]  # pobranie klasyfikatora dla konkretnego podzbioru i k
                prediction = classifier.predict_proba(X_splitted[s_index])[:, 1]  # predykcja dla konkretnego przedziału
                predictions[:, k_index] = prediction  # zapisanie w tablicy predykcji
            interval = np.column_stack((predictions.min(axis=1), predictions.max(
                axis=1)))  # wybór minimalnej i maksymalnej wartości (przedziału) dla każdego elementu
            intervals[:, s_index] = interval  # zapis przedziału
        predictions = self.__get_predictions(intervals)  # agregacja i określenie klasy

        return predictions

    def score(self, X, y, sample_weight=None):
        return self.score_acc(X, y, sample_weight)

    def score_acc(self, X, y, sample_weight=None):
        predictions = self.predict(X)
        # print(predictions)
        score_acc = self.__score__acc(y, predictions, X)
        score_coverage = self.__score_coverage(predictions)
        score_u_area = self.__score_u_area(predictions)

        print('scores:', score_acc, score_coverage, score_u_area)
        return score_acc, score_coverage, score_u_area

    def __set_classifiers(self):
        self.classifiers = [
            [KNeighborsClassifier(n_neighbors=self.k[k_index], n_jobs=self.n_jobs) for k_index in range(len(self.k))]
            for _ in range(self.s)
        ]  # tablica klasyfikatorów knn o wymiarach s i długości tablicy k

    def __split_dataset(self, X):
        return np.array_split(X, self.s, axis=1)  # podział na s podzbiorów

    def __get_predictions(self, intervals):
        result = []
        for interval in intervals:  # interval - lista s przedziałów [down(u), up(u)] dla obiektu u
            aggregation = self.aggregation(interval)  # agregacja przedziałów, wynik [down(u), up(u)]
            result.append(aggregation)
        return np.array(result)

    def __score__acc(self, y, predictions, X):
        predictions_array = np.array(predictions)
        filter_indices = np.where(
            predictions_array != -1)  # wyszukanie indeksów gdzie nie ma obiektów niesklasyfikowanych
        y_filtered = y[filter_indices] #.tolist()  # filtrowanie rzeczywistych klas po wyszukanych indeksach
        predictions_filtered = predictions_array[
            filter_indices]  # filtrowanie predykcji po wyszukanych indeksach
        return metrics.accuracy_score(y_filtered, predictions_filtered)

    def __score_coverage(self, predictions):
        return 1 - self.__score_u_area(predictions)

    def __score_u_area(self, predictions):
        predictions = predictions.tolist()
        return predictions.count(-1) / len(predictions)  # liczba niesklasyfikowanych / liczba wszystkich obiektów
