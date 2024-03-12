import matplotlib.pyplot as plt
import matplotlib
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

matplotlib.rcParams.update({'font.size': 14})


plt.subplot(311)
plt.gca().patch.set_alpha(0.0)
plt.text(0.5, 0.2, 't=0.5')
# plt.fill_between([0.2, 0.4], 0, 0.02)
plt.fill_between([0.2, 0.4], 0, 0.05)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.yticks([])

for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().tick_params(width=2, length=7)
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0)], s=100)

plt.subplot(312)
plt.gca().patch.set_alpha(0.0)
plt.fill_between([0.4, 0.6], 0, 0.05)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.text(0.5, 0.2, 't=0.5')
plt.yticks([])
for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().tick_params(width=2, length=7)
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0, 0.5)], s=100)

plt.subplot(313)
plt.gca().patch.set_alpha(0.0)
plt.fill_between([0.6, 0.8], 0, 0.05)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.text(0.5, 0.2, 't=0.5')
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0)], s=100)
#plt.yticks([])
plt.tick_params(axis='y', which='both', right=False,
                left=False, labelleft=False)
for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().tick_params(width=2, length=7)
plt.show()