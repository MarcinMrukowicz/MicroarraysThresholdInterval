import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

fig, axes = plt.subplots(3, 2)
fig.set_size_inches(10, 3)
intervals = [(0.2, 0.4), (0.4, 0.6), (0.6, 0.8)]
descriptions = [
    "Treshold t=0.5 and interval range\n"
    "from 0.2 to 0.4. Interval is below treshold\n"
    "and object will be labeled as negative.",
    "Treshold t=0.5 and interval range\n"
    "from 0.4 to 0.6. Treshold is inside the interval\n"
    "so we cannot say that object have negative\n"
    "or positive label.",
    "Treshold t=0.5 and interval range\n"
    "from 0.6 to 0.8. Interval is above treshold\n"
    "and object will be labeled as positive.",
]
for ax, ax_col1, interval, description in zip(axes[:, 0], axes[:, 1], intervals, descriptions):
    ax.set_yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(1)
    # ax.figure.set_size_inches(5, 0.3)

    ax_col1.spines['top'].set_visible(False)
    ax_col1.spines['left'].set_visible(False)
    ax_col1.spines['right'].set_visible(False)
    ax_col1.spines['bottom'].set_visible(False)
    ax_col1.set_xticks([])
    ax_col1.set_yticks([])

    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])

    ax.set_ylim(0, 0.5)

    # DRAW INTERVAL
    rectangle = patches.Rectangle((interval[0], 0), interval[1] - interval[0], 0.1, linewidth=0, edgecolor='tab:blue',
                                  facecolor='tab:blue')
    ax.add_patch(rectangle)

    # DRAW TRESHOLD
    rectangle = patches.Rectangle((0.5, 0), 0, 0.2, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rectangle)

    # Custom legend
    legend_labels = ['Interval', 'treshold']
    legend_handles = [plt.Rectangle((0, 0), 1, 1, fc="tab:blue"), Line2D([0], [0], color='red', lw=1)]
    axes[0,0].legend(legend_handles, legend_labels, loc='lower right')

    # DRAW t=0.5
    ax.text(0.5, 0.3, 't=0.5', fontsize=12, ha='center', va='center')

    # DRAW DESCRIPTION
    ax_col1.text(0,0, description, fontsize=12)
    # ax.figure.set_size_inches(10, 3)
# Save the plot as an SVG file
plt.tight_layout()
plt.subplots_adjust(left=0.02, right=1, top=1, bottom=0.1)
plt.savefig('img/plot.svg', format='svg')
plt.show()

