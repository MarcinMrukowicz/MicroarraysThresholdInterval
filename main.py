import numpy as np
from sklearn.feature_selection import RFE
from sklearn.model_selection import GridSearchCV
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
                             n_features_to_select=0.1)))
    steps.append(('algorithm', Algorithm(s=10, k=[3, 5, 7], t=0.5, aggregation=A1, random_state=seed, n_jobs=-1)))

    pipe = Pipeline(steps)
    param_grid = {}

    search = GridSearchCV(pipe, param_grid, n_jobs=-1)
    search.fit(dataset.X, dataset.y)
    print(search.best_score_)
