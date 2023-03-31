import numpy as np
from sklearn.feature_selection import RFE
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import SVC

from aggregations import A1
from algorithm import Algorithm
from dataset import Dataset

seed = np.random.RandomState(0)
dataset = Dataset('colonTumor')

if __name__ == '__main__':
    steps = []
    steps.append(('scaler', RobustScaler()))
    steps.append(('rfe', RFE(estimator=SVC(kernel='linear', random_state=seed), step=1,
                             n_features_to_select=0.1))) # wybranie 10% cech
    # ustawiono na sztywno próg t, do policzenia accuracy warto zbadać różne progi, zwłaszcza jakby
    # wyniki nie wychodziły bardzo dobrze
    # agregacja na razie jest jedna
    steps.append(('algorithm', Algorithm(s=50, k=[3, 5, 7], t=0.4, aggregation=A1, random_state=seed, n_jobs=-1)))


    # tutaj ustawiono seed - do pracy można z tego zrezygnować, albo uruchomić dla różnych seedów
    cv = StratifiedKFold(n_splits=5, random_state=1, shuffle=True)

    results = []

    for (train_index, test_index) in cv.split(X=dataset.X, y=dataset.y):
        pipe = Pipeline(steps)

        pipe.fit(dataset.X.iloc[train_index], dataset.y[train_index])
        results.append(pipe.score(dataset.X.iloc[test_index], dataset.y[test_index]))

# tutaj pewnie jakoś pasuje do excela eksportować wyniki
# strukturę danych ze zwykłej krotki można zmienić na słownik, albo named tuple
# jeżeli będzie dogodniej
    print(results)
    results = np.array(results)
    print('results_as_numpy_array', results)
    print('mean accuracy', np.mean(results[:, 0]))
    print('mean coverage', np.mean(results[:, 1]))
    print('mean UArea', np.mean(results[:, 2]))
