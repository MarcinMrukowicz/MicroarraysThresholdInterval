import numpy as np
from sklearn import metrics

from dataset import Dataset

s_list = [2, 5, 10, 15, 20, 30, 50, 70, 100, 150]

datasets = [Dataset('AMLALL_Total', 1),
            Dataset('colonTumor', 1),
            Dataset('DLBCL-Stanford', 1),
            Dataset('ovarian_61902', 500),
            Dataset('prostate_TumorVSNormal_Total', 500)
            ]


def score__acc(y, predictions, X):
    predictions_array = np.array(predictions)
    filter_indices = np.where(
        predictions_array != -1)  # selecting not labelled instances
    y_filtered = y[filter_indices]
    predictions_filtered = predictions_array[
        filter_indices]
    return metrics.accuracy_score(y_filtered, predictions_filtered)

def score_coverage(predictions):
    return 1 - score_u_area(predictions)

def score_u_area(predictions):
    predictions = predictions.tolist()
    return predictions.count(-1) / len(predictions)