import numpy as np
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from sklearn.base import TransformerMixin, BaseEstimator

pandas2ri.activate()
robjects.r.source('glscaleR.R')


class Glscale(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        arr = np.array(robjects.r('glscale')(X)[0])
        index = np.isnan(arr).any(axis=0)
        arr[:, index] = 0
        return arr
