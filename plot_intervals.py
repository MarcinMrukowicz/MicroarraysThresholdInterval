import matplotlib.pyplot as plt

plt.subplot(311)
plt.text(0.2, 0.2, '[0.2, 0.4]')
plt.text(0.5, 0.2, 't=0.5')
plt.fill_between([0.2, 0.4], 0, 0.02)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.yticks([])
for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0)])

plt.subplot(312)
plt.fill_between([0.4, 0.6], 0, 0.02)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.text(0.5, 0.2, 't=0.5')
plt.yticks([])
for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0, 0.5)])

plt.subplot(313)
plt.fill_between([0.6, 0.8], 0, 0.02)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.text(0.5, 0.2, 't=0.5')
plt.scatter([0.5], 0, c=[(1.0, 0.0, 0.0)])
#plt.yticks([])
plt.tick_params(axis='y', which='both', right=False,
                left=False, labelleft=False)
for pos in ['right', 'top', 'left']:
    plt.gca().spines[pos].set_visible(False)
plt.show()