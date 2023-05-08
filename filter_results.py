import numpy as np
import pandas as pd

pd.set_option('display.max_colwidth', 100000000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.precision', 3)


datasets = ['./RESULTS_AML_ALL_final_v3.xlsx', './RESULTS_COLON_final_v3.xlsx', './RESULTS_DLBCL_final_v3.xlsx',
            './RESULTS_prostate_final_v3.xlsx', './RESULTS_ovarian_final_v3.xlsx']

accuracy_thresholds = [0.98, 0.86, 0.9, 0.92, 0.99]
coverage_thresholds = [0.95, 0.86, 0.85, 0.85, 0.99]


def filter_function(x):
    if 'KNeighborsClassifier' not in x:
        return x.split('.')[1].split(' ')[0].replace('Aggregation', '')
    return np.NAN


for i, d in enumerate(datasets):
    print(d)
    data = pd.read_excel(d)
    print(data.shape)
    data['aggregation'] = data['algorithm'].apply(filter_function)
    data.to_excel(d+'_improved.xlsx', index=None)

    accuracy_threshold = accuracy_thresholds[i]
    coverage_threshold = coverage_thresholds[i]

    # filtered data to be above both thresholds
    filtered = data[(data['accuracy'] > accuracy_threshold) & (data['coverage'] > coverage_threshold)]

    # select columns
    print(filtered[['aggregation', 'k', 's', 't', 'accuracy', 'coverage']])
    print(filtered.shape)
    # take 20 best and export to latex table
    filtered[['aggregation', 'k', 's', 't', 'accuracy', 'coverage']].iloc[:20, :].to_latex(d + '.tex', index=None)

    # here create summaries for the best aggregations
    # the threshold could be lower here, because we want
    # more global overview
    filtered = data[(data['accuracy'] > 0.8) & (data['coverage'] > 0.8)]
    filtered2 = filtered[['aggregation', 'k', 't', 'accuracy', 'coverage']].groupby(['aggregation', 'k'])\
        .aggregate({'accuracy': ['count', 'mean', 'std'], 'coverage': ['mean', 'std']})
    print(filtered2)
    filtered2.to_latex(d+'_aggs_.tex')



