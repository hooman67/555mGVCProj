import random
import numpy as np
import matplotlib.pyplot as plt

# fake data
fs = 10  # fontsize
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]

#fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))
fig = plt.figure(figsize=(9, 9))

plt.violinplot(data, pos, points=20, widths=0.3,
                      showmeans=True, showextrema=True, showmedians=True)
#axes[0].set_title('Custom violinplot 1', fontsize=fs)



'''for ax in axes:
    ax.set_yticklabels([])'''

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()