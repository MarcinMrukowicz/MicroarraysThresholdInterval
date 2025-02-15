import os

import pandas as pd
from sklearn import preprocessing


class Dataset():
    def __init__(self, name, rfe_step):
        self.rfe_step = rfe_step
        self.name = name
        self.X = self.__read_dataset()
        self.y = self.__transform_labels(self.__read_labels())

    def __read_dataset(self):
        return pd.read_csv(
            filepath_or_buffer=os.path.join(os.path.dirname(__file__), "datasets/" + self.name + "DATA.csv"),
            header=None)

    def __read_labels(self):
        return pd.read_csv(
            filepath_or_buffer=os.path.join(os.path.dirname(__file__), "datasets/" + self.name + "LABELS.csv"),
            header=None)

    def __transform_labels(self, labels):
        label_encoder = preprocessing.LabelEncoder()
        return label_encoder.fit_transform(labels.values.ravel())

    def __drop_na_cols(self, data):
        return data.apply(pd.to_numeric, errors='coerce').dropna(axis=1)
