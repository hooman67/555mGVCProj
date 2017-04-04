import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import radio_test


alternatives = ('Ritz', "Day's Inn", 'Basement')
segments = 4
users = ['Emily', 'Ann', 'Bob', 'Carol']
data = [ [80,60, 20], [100, 0, 0], [100, 51, 0], [68, 89, 38]]

opacity = 0.66
test_percents = []
for i in data:
    for x in i:
        test_percents.append(x)
print test_percents        

# generate some multi-dimensional data & arbitrary labels
#data = 3 + 10* np.random.rand(segments, len(alternatives))

#percentages = (np.random.randint(5,20, (len(alternatives), segments)))

y_pos = np.arange(len(alternatives))
print y_pos

fig = plt.figure(figsize=(12,9))
fig.subplots_adjust(top=0.85)
ax = fig.add_subplot(111)

ax.xaxis.grid(True, linestyle='--', which='major',
                   color='grey')
colors ='rgbcwm'
patch_handles = []
left = np.zeros(len(alternatives)) # left alignment of data starts at zero

for i, d in enumerate(data):
    #print i
    #print d
    patch_handles.append(ax.barh(y_pos, d, height = 0.33, label=users[i],
      color=colors[i%len(colors)], align='center', alpha=opacity,
      left=left))
    # accumulate the left-hand offsets
    #left += d
    
    left += 100 #Offset needs to be user weight???
    
count = 0
# go through all of the bar segments and annotate
for j in xrange(len(patch_handles)):
    for i, patch in enumerate(patch_handles[j].get_children()):
        bl = patch.get_xy()
        x = 0.5*patch.get_width() + bl[0]
        y = 0.5*patch.get_height() + bl[1]
        #ax.text(x,y, "%d%%" % (percentages[i,j]), ha='center')
        ax.text(x,y, "%d%%" % (test_percents[count]), ha='center')
        count += 1

ax.set_yticks(y_pos)
ax.set_yticklabels(alternatives)
#ax.xaxis.set_ticks([0, 100, 200])
ax.set_xticklabels([''])
loc = plticker.MultipleLocator(base=100)
ax.xaxis.set_major_locator(loc)
ax.set_xlabel('Total Scores')


leg = ax.legend(loc="upper left", bbox_to_anchor=[0, 1.2],
           ncol=2, shadow=True, title="Legend", fancybox=True)

for label in ax.get_yticklabels():  # make the xtick labels pickable
    label.set_picker(True)
for lege in leg.get_texts():
    lege.set_picker(5)

def onpick(event):
    legline = event.artist
    #origline = spoke_labels[legline]
    
    if legline.get_text() == alternatives[0]:
      radio_test.main("Ritz")
    elif legline.get_text() == alternatives[1]:
      radio_test.main("Days Inn")
    elif legline.get_text() == alternatives[2]:
      radio_test.main("Basement")
    else:
      print str(legline.get_text())
   
fig.canvas.mpl_connect('pick_event', onpick)

plt.show()

