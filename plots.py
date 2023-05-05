import copy

import matplotlib.pyplot as plt
import numpy as np

from aggregations import A1Aggregation, A2Aggregation, A3Aggregation, A4Aggregation, A5Aggregation, A6Aggregation, A7Aggregation, A8Aggregation, A9Aggregation, A10Aggregation

a = A1Aggregation().aggregate_numpy_arrays_representation(np.array([[0.1, 0.7], [0.3, 0.6], [0.3, 0.6]]))

x = np.linspace(0, 1.0, num=11)
y = np.linspace(0, 1.0, num=11)
X,Y = np.meshgrid(x, y)


aggregation_func = [A1Aggregation, A2Aggregation, A3Aggregation, A4Aggregation, A5Aggregation, A6Aggregation, A7Aggregation, A8Aggregation, A9Aggregation, A10Aggregation]
for func in aggregation_func:
    Z1 = copy.copy(X)
    Z2 = copy.copy(X)
    for i in range(len(X)):
        for j in range(len(X[1])):
            aggregated = func().aggregate_numpy_arrays_representation(np.array([[X[i,j], X[i,j]], [Y[i,j],Y[i,j]]]))
            Z1[i,j] = aggregated[0]
            Z2[i,j] = aggregated[1]

    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,alpha=0.7,
                    color="red", edgecolor='none')
    ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.7,
                    color="blue", edgecolor='none')
    plt.title(func.change_aggregation_to_name(func()))
    ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    ax.set_xticks(ticks)
    ax.set_xticklabels([str([round(i,2), round(i,2)]) for i in ticks], rotation = 10,
                       verticalalignment='baseline',
                       horizontalalignment='right'
                       )
    ax.set_yticks(ticks)
    ax.set_yticklabels([str([round(j,2), round(j,2)]) for j in ticks] , rotation = -10,
                       verticalalignment='baseline',
                       horizontalalignment='left')
    plt.savefig(f"img/{func.change_aggregation_to_name(func())}.jpg")
    plt.show()

print(Y)

