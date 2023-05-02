from statistics import stdev

import numpy as np
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold, LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import SVC
from sklearn.impute import KNNImputer
from sklearn.tree import DecisionTreeClassifier

from aggregations import *
from algorithm import Algorithm
from dataset import Dataset

seed = np.random.RandomState(0)
#dataset = Dataset('ovarian_61902')
dataset = Dataset('DLBCL-Stanford')

if __name__ == '__main__':
    steps = []
    steps.append(('scaler', ))
    steps.append(('rfe', RFE(estimator=SVC(kernel='linear', random_state=seed), step=1,
                             n_features_to_select=0.1))) # wybranie 10% cech
    # ustawiono na sztywno próg t, do policzenia accuracy warto zbadać różne progi, zwłaszcza jakby
    # wyniki nie wychodziły bardzo dobrze
    # agregacja na razie jest jedna
    steps.append(('algorithm', Algorithm(s=50, k=[3, 5, 7], t=0.8, aggregation=A1Aggregation(), random_state=seed, n_jobs=-1)))


    # tutaj ustawiono seed - do pracy można z tego zrezygnować, albo uruchomić dla różnych seedów
    cv = LeaveOneOut() #StratifiedKFold(n_splits=2, random_state=1, shuffle=True)

    algorithms = []

    for s in [2, 5, 10, 15, 20, 30, 50]:
        for k in ([1],):
            for a in [A1Aggregation(), A3Aggregation(), A4Aggregation(), A5Aggregation(), A6Aggregation(), A8Aggregation(), A9Aggregation(), A10Aggregation()]:
                for t in (0.4, 0.5, 0.6): #(0.4, 0.45, 0.5, 0.55, 0.6):
                    algorithms.append(Algorithm(s=s, k=k, aggregation=a, t=t, n_jobs=-1, random_state=seed))

    for s in [2, 5, 10, 15, 20, 30, 50]:
        for k in ([1, 2],):
            for a in [A1Aggregation(), A2Aggregation(), A3Aggregation(), A4Aggregation(), A5Aggregation(), A6Aggregation(), A7Aggregation(), A8Aggregation(), A9Aggregation(), A10Aggregation()]:
                for t in (0.4, 0.5, 0.6): #(0.4, 0.45, 0.5, 0.55, 0.6):
                    algorithms.append(Algorithm(s=s, k=k, aggregation=a, t=t, n_jobs=-1, random_state=seed))

    algorithms += [
        KNeighborsClassifier(n_neighbors=1),
        KNeighborsClassifier(n_neighbors=2),
        KNeighborsClassifier(n_neighbors=3),
        KNeighborsClassifier(n_neighbors=5)
    ]



    result = []
    for i in range(len(algorithms)):
        result.append([])

    j = 0

    for (train_index, test_index) in cv.split(X=dataset.X, y=dataset.y):
        imputer = None
        dataset.X = dataset.X.where(dataset.X != ' ?', None)
        print(dataset.X.iloc[1][3])
        print(dataset.X)
        contains_missing = dataset.X.iloc[train_index].isnull().values.any()
        train_data = dataset.X.iloc[train_index]

        if contains_missing:
            print('contains missing')
            print(train_data[:20])
            imputer = KNNImputer(n_neighbors=1)
            imputer.fit(train_data)
            imputed_X = imputer.transform(train_data)
            train_data = imputed_X

        scaller = RobustScaler()
        scaller.fit(train_data, dataset.y[train_index])
        X_scaled = scaller.transform(train_data)

        rfe = RFE(estimator=SVC(kernel='linear', random_state=seed), step=1000,
                  n_features_to_select=0.1)
        rfe.fit(X_scaled, dataset.y[train_index])
        X_filtered = rfe.transform(X_scaled)
        print('train y', dataset.y[train_index])

        test_data = dataset.X.iloc[test_index]
        contains_missing_in_test = test_data.isnull().values.any()
        if contains_missing_in_test:
            imputed_test_X = imputer.transform(dataset.X.iloc[test_index])
            test_data = imputed_test_X

        scalled_test = scaller.transform(test_data)
        filtered_test = rfe.transform(scalled_test)

        for i, est in enumerate(algorithms):
            if len(result[i]) == 0: result[i].append(str(est))
            est.fit(X_filtered, dataset.y[train_index])

            print('true y labels', dataset.y[test_index])
            result[i].append(est.score(filtered_test, dataset.y[test_index]))
            print(est.predict(filtered_test))
            print(result)
        j += 1


    # tutaj pewnie jakoś pasuje do excela eksportować wyniki
    # strukturę danych ze zwykłej krotki można zmienić na słownik, albo named tuple
    # jeżeli będzie dogodniej



    final_results = []
    for i in range(len(algorithms)):
        results = np.array(result[i][1:])

        if 'Algorithm' in result[i][0]:
            w = pd.DataFrame({'algorithm': result[i][0], 'agg': str((algorithms[i].aggregation)),
                              'accuracy': np.nanmean(results[:, 0]), 'k': str(algorithms[i].k),
                              's': algorithms[i].s, 't': algorithms[i].t,
                              'coverage': np.mean(results[:, 1]), 'UArea': np.mean(results[:, 2])
                              }, index=[i])
            print(w)
            final_results.append(w)
        else:
            final_results.append(pd.DataFrame({'algorithm': result[i][0],
                                               'agg': np.NAN,
                                               'accuracy': np.mean(results),
                                               'k': np.NAN,
                                               's': np.NAN,
                                               't': np.NAN,
                                               'coverage': np.NAN,
                                               'UArea': np.NAN
                                               }, index=[i]))


        print('results_as_numpy_array', results)
        # print('mean accuracy', np.nanmean(results[:, 0]))
        # print('mean coverage', np.mean(results[:, 1]))
        # print('mean UArea', np.mean(results[:, 2]))

fin_res = pd.concat(final_results)
print(fin_res)
fin_res.to_excel('RESULTS_dlbcl.xlsx')