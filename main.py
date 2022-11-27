import os

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC

from aggregations import A1
from dataset import Dataset

random_state = np.random.RandomState(0)
normalizer = preprocessing.Normalizer()
estimator = SVC(kernel='linear', random_state=random_state)

dataset = Dataset('colonTumor')

step = 1
min_features_to_select = 20
s = 20
R = [3, 5, 7, 9]
t = 0.5


def get_ranking_filename(dataset_name, type):
    return "cache/" + dataset_name + "_RFECV_ranking_" + type + ".csv"


def get_ranking(X, y, dataset_type):
    try:
        return pd.read_csv(
            filepath_or_buffer=os.path.join(os.path.dirname(__file__),
                                            get_ranking_filename(dataset.name, dataset_type)),
            header=None).transpose().to_numpy()[0]
    except FileNotFoundError:
        estimator.fit(X, y)
        selector = RFECV(estimator, step=step, min_features_to_select=min_features_to_select,
                         n_jobs=-1)
        selector = selector.fit(X, y)
        ranking = selector.ranking_
        pd.DataFrame(ranking).to_csv(get_ranking_filename(dataset.name, dataset_type), header=False, index=False)
        return ranking


def get_subtables(X, ranking):
    sorted_idx = np.argsort(ranking)
    idx_mask = (ranking[sorted_idx] == 1)
    sorted_filtered_idx = sorted_idx[idx_mask]
    filtered_x = np.take(a=X, indices=sorted_filtered_idx, axis=1)
    return np.array_split(filtered_x, s, axis=1)


if __name__ == '__main__':
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.dataset, dataset.labels, random_state=random_state)

    X_train = normalizer.transform(X_train)
    X_test = normalizer.transform(X_test)

    ranking_train = get_ranking(X_train, y_train, 'train')
    ranking_test = get_ranking(X_test, y_test, 'test')

    X_subtables = get_subtables(X_train, ranking_train)

    intervals = np.empty((len(X_train), s, 2))
    for X_subtable_idx, X_subtable in enumerate(X_subtables):
        predictions = np.empty((len(X_train), len(R)))
        for n_neighbors_idx, n_neighbors in enumerate(R):
            knn = KNeighborsRegressor(n_neighbors=n_neighbors)
            knn.fit(X_subtable, y_train)
            prediction = np.array(knn.predict(X_subtable))
            predictions[:, n_neighbors_idx] = prediction
        predictions_min = predictions.min(axis=1)
        predictions_max = predictions.max(axis=1)
        interval = np.column_stack((predictions_min, predictions_max))
        intervals[:, X_subtable_idx] = interval

    result = []
    for interval in intervals:
        aggregation = A1(interval)
        if t < aggregation[0]:
            result.append(0)
        elif t > aggregation[1]:
            result.append(1)
        else:
            result.append(None)

    print(result)

    UArea = result.count(None) / len(result)

    print(UArea)
