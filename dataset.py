import os

import numpy as np
import pandas as pd
from sklearn import preprocessing
import re

class Dataset():
    def __init__(self, name, outliers:list = None):
        self.name = name
        self.X = self.__read_dataset()
        self.y = self.__transform_labels(self.__read_labels())
        if outliers is not None:
            indexes = self.__drop_outliers(self.__read_labels().to_numpy().ravel(), outliers)
            self.X = self.X.drop(indexes)
            self.y = np.delete(self.y, indexes, None)
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


    def __drop_outliers(self, labels, outliers):
        '''
        Function that finds index of element by pattern e.g. 1T finds first occurence of label starts with T,
        2Ta finds first occurence of label starts with Ta,
        '''
        # split outliets into number and pattern
        number = []
        pattern = []
        for outlier in outliers:
            number.append(re.findall(r'\d+', outlier)[0])
            pattern.append(re.search(r'\d+\s*(\w+)', outlier).group(1))
        # print(number,pattern)
        # get outlier indexes
        outliers_index = []
        counter = dict()
        for index,  label in enumerate(labels):
            # Update counter
            if label in counter.keys():
                counter[label] = counter[label] + 1
            else:
                counter[label] = 1
            # print(counter)
            for j, num in enumerate(number):
                if int(num) == int(counter[label])and label.startswith(pattern[j]):
                    outliers_index.append(index)
        # print(outliers_index)
        return outliers_index
