import random
import numpy as np
import matplotlib.pyplot as plt

# fake data
fs = 10  # fontsize
pos = [1, 2, 4, 5, 7, 8]
pos = [1, 2, 3, 4]
#pos = ['Pool', 'Internet', 'Location']
#data = [np.random.normal(0, std, size=100) for std in pos]
data = [[0, 0, 0.3], [0.8, 0, 0.3], [0.2, 1, 0.4], [0.61, 0.27, 0.11]]
data = np.array(data)
print data

#fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 6))
fig = plt.figure(figsize=(9, 9))

plt.violinplot(data, points=20, widths=0.3,
                      showmeans=True, showextrema=False, showmedians=False)
#axes[0].set_title('Custom violinplot 1', fontsize=fs)



'''for ax in axes:
    ax.set_yticklabels([])'''

#fig.suptitle("Violin Plotting Examples")

fig.subplots_adjust(hspace=0.4)
plt.show()