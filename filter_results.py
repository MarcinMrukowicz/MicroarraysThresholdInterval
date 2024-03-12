import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

    data_to_plot = filtered[['aggregation', 'k', 's', 't', 'accuracy', 'coverage']].iloc[:20, :]
    data_to_plot.to_excel(d + '_plots.xlsx', index=None)

    labels = []
    accuracies = []
    coverages = []
    print(data_to_plot.iloc[0, 0])

    # here create figures used in supplementary materials
    plots_no = 0
    while plots_no < 4:
        labels = []
        accuracies = []
        coverages = []
        for i in range((plots_no * 5), (plots_no * 5) + 5):
            label = data_to_plot.iloc[i, 0] + ', k = ' + str(data_to_plot.iloc[i, 1]) + ', s = ' + str(data_to_plot.iloc[i, 2]) + ', t = ' \
                + str(data_to_plot.iloc[i, 3])
            labels.append(label)
            accuracies.append(data_to_plot.iloc[i, 4])
            coverages.append(data_to_plot.iloc[i, 5])

        x = np.arange(len(labels))

        props = dict(boxstyle='round', facecolor='black', alpha=0.5)

        fig, ax = plt.subplots(layout='constrained')
        width = 0.25

        rects = ax.barh(x, accuracies, width, label='accuracy')
        ax.bar_label(rects, padding=3)

        rects = ax.barh(x + width, coverages, width, label='coverage')
        ax.bar_label(rects, padding=3)

        for i, s in enumerate(labels):
            ax.text(0.62, 0.1 + (i), s, fontsize=12, bbox=props, color='white')

        ax.set_yticks(x + width, np.array(['' for i in range(len(labels))]))
        ax.legend(loc='upper left', ncols=3)
        ax.set_xlim(0.6, 1.05)
        ax.invert_yaxis()
        plt.title(d.split('_')[1] if d.split('_')[1] != 'AML' else 'AML ALL')
        plt.show()
        plots_no += 1



    # here create summaries for the best aggregations
    # the threshold could be lower here, because we want
    # more global overview
    filtered = data[(data['accuracy'] > 0.8) & (data['coverage'] > 0.8)]
    filtered[['aggregation', 'k', 't', 'accuracy', 'coverage']].to_excel(d+'_aggs.xlsx', index=False)
    print(filtered[['aggregation', 'k', 't', 'accuracy', 'coverage']])
    filtered2 = filtered[['aggregation', 'k', 't', 'accuracy', 'coverage']].groupby(['aggregation', 'k'])\
        .aggregate({'accuracy': ['count', 'mean', 'std'], 'coverage': ['mean', 'std']})
    print(filtered2)
    filtered2.to_latex(d+'_aggs_.tex')



