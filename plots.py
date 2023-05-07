import copy

import matplotlib.pyplot as plt
import numpy as np

from aggregations import A1Aggregation, A2Aggregation, A3Aggregation, A4Aggregation, A5Aggregation, A6Aggregation, A7Aggregation, A8Aggregation, A9Aggregation, A10Aggregation

a = A1Aggregation().aggregate_numpy_arrays_representation(np.array([[0.1, 0.7], [0.3, 0.6], [0.3, 0.6]]))

x = np.linspace(0, 1.0, num=11)
y = np.linspace(0, 1.0, num=11)
X,Y = np.meshgrid(x, y)


aggregation_func = [A1Aggregation, A2Aggregation, A3Aggregation, A4Aggregation, A5Aggregation, A6Aggregation, A7Aggregation, A8Aggregation, A9Aggregation, A10Aggregation]
# for func in aggregation_func:
#     Z1 = copy.copy(X)
#     Z2 = copy.copy(X)
#     for i in range(len(X)):
#         for j in range(len(X[1])):
#             aggregated = func().aggregate_numpy_arrays_representation(np.array([[X[i,j], X[i,j]], [Y[i,j],Y[i,j]]]))
#             Z1[i,j] = aggregated[0]
#             Z2[i,j] = aggregated[1]
#
#     ax = plt.axes(projection='3d')
#     ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,alpha=0.7,
#                     color="red", edgecolor='none')
#     ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.7,
#                     color="blue", edgecolor='none')
#     plt.title(func.change_aggregation_to_name(func()))
#     ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
#     ax.set_xticks(ticks)
#     ax.set_xticklabels([str([round(i,2), round(i,2)]) for i in ticks], rotation = 10,
#                        verticalalignment='baseline',
#                        horizontalalignment='right'
#                        )
#     ax.set_yticks(ticks)
#     ax.set_yticklabels([str([round(j,2), round(j,2)]) for j in ticks] , rotation = -10,
#                        verticalalignment='baseline',
#                        horizontalalignment='left')
#     plt.savefig(f"img/{func.change_aggregation_to_name(func())}.jpg")
#     plt.show()
#
# print(Y)

x = np.linspace(0,1.0,5)
x1 = [[0,0], [0,0.5], [0,1], [0.5, 1.0], [1,1]]
y = np.linspace(0,1.0,5)
x2 = [[0,0], [0,0.5], [0,1], [0.5, 1.0], [1,1]]
X,Y = np.meshgrid(x, y)

for func in aggregation_func:
    ax = plt.axes(projection='3d')
    Z1 = copy.copy(X)
    Z2 = copy.copy(X)
    for i,val_i in enumerate(x):
        for j, val_j in enumerate(y):
            aggregated = func().aggregate_numpy_arrays_representation(np.array([x1[i], x2[j]]))
            Z1[i,j] = aggregated[0]
            Z2[i,j] = aggregated[1]
            ax.plot3D([val_i,val_i], [val_j,val_j],[aggregated[0],aggregated[1]], color="black")

    ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,alpha=0.2,
                    color="blue", edgecolor='none')
    ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.2,
                    color="red", edgecolor='none')
    plt.title(func.change_aggregation_to_name(func())+" k(1,2)")
    ticks = x
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(i) for i in x1], rotation = 10,
                       verticalalignment='baseline',
                       horizontalalignment='right'
                       )
    ax.set_yticks(ticks)
    ax.set_yticklabels([str(j) for j in x2] , rotation = -10,
                       verticalalignment='baseline',
                       horizontalalignment='left')
    plt.savefig(f"img/k=1,2{func.change_aggregation_to_name(func())}.jpg")
    plt.show()


k = [2,3]
possible_coefficients = set()
for k_ in k:
    for i in range(len(k)+1):
        possible_coefficients.add(round(i/k_,4))
possible_coefficients = list(possible_coefficients)
possible_coefficients.sort()
print(possible_coefficients)

intervals=[]
for i in possible_coefficients:
    for j in possible_coefficients:
        interval = ((min([i,j]), max([i,j])))
        if interval not in intervals:
            intervals.append(interval)

print(intervals)

x = np.linspace(0,1.0,len(intervals))
x1 = intervals
y = np.linspace(0,1.0,len(intervals))
x2 = intervals
X,Y = np.meshgrid(x, y)

for func in aggregation_func:
    ax = plt.axes(projection='3d')
    Z1 = copy.copy(X)
    Z2 = copy.copy(X)
    for i,val_i in enumerate(x):
        for j, val_j in enumerate(y):
            aggregated = func().aggregate_numpy_arrays_representation(np.array([x1[i], x2[j]]))
            Z1[i,j] = aggregated[0]
            Z2[i,j] = aggregated[1]
            ax.plot3D([val_i,val_i], [val_j,val_j],[aggregated[0],aggregated[1]], color="black")

    ax.plot_surface(X, Y, Z1, rstride=1, cstride=1,alpha=0.2,
                    color="blue", edgecolor='none')
    ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.2,
                    color="red", edgecolor='none')
    plt.title(func.change_aggregation_to_name(func())+" k(1,2,3)")
    ticks = x
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(i) for i in x1], rotation = 10,
                       verticalalignment='baseline',
                       horizontalalignment='right'
                       )
    ax.set_yticks(ticks)
    ax.set_yticklabels([str(j) for j in x2] , rotation = -10,
                       verticalalignment='baseline',
                       horizontalalignment='left')
    plt.savefig(f"img/k=1,2,3{func.change_aggregation_to_name(func())}.jpg")
    plt.show()
