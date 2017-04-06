import random
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
from itertools import repeat

def main(user_data):
    red_patch = mpatches.Patch(color='red')

    users = []
    for i in range(len(user_data)):
        users.append(user_data[i][0])
    criteria = []
    for i in user_data[0][1].iterkeys():
        criteria.append(i)
    print criteria
    weight = []
    for a in range(len(criteria)):
        temp = []
        val = criteria[a]
        for i in range(len(user_data)):
            temp.append(int(float(user_data[i][1][val])*100))
        weight.append(temp)
    print weight
        



    # 'fake' invisible object

    #pos   = [1, 2, 4, 5, 7, 8]
    pos = np.arange(0, len(criteria))
    #label = ['plot 1','plot2','ghi','jkl','mno','pqr']
    #data  = [np.random.normal(size=100) for i in pos]
    data = [[0, 0.8, 0.3], [0.2, 0.6, 0.4], [1, 0.2, 0.3], [0.4, 0.5, 0.8]]

    #fake_handles = repeat(red_patch, len(pos))

    pl.figure()
    ax = pl.subplot(111)
    ax.set_title('title')
    pl.violinplot(weight, pos, showmeans=True, showextrema=False, showmedians=False)
    #ax.legend(fake_handles, label)
    pl.show()