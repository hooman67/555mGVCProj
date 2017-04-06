import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import radio_test
import radio_user
import scenarioAB_Processing
import vio_test


'''alternatives = ('Ritz', "Day's Inn", 'Basement')
segments = 4
users = ['Emily', 'Ann', 'Bob', 'Carol', 'Total']
data = [ [80,60, 20], [100, 0, 0], [100, 51, 0], [68, 89, 38], [87, 50, 15]] #show this as combined bars or portion of 100?'''
xml_name = str(sys.argv[1])

#print user_data
alternatives = scenarioAB_Processing.get_alt_data(xml_name)
print alternatives
user_data  = scenarioAB_Processing.get_user_data(xml_name)
print user_data
#print alternatives

data = scenarioAB_Processing.get_total_values(user_data, alternatives) #code dies here with continuous values
print data
for i in range(len(data)):
    for x in range(len(data[i])):
        #data[i][x] = 100* (round(data[i][x]), 2)
        data[i][x] = round(data[i][x] * 100)

users = []
for i in range(len(user_data)):
    users.append(user_data[i][0])
#users = users[::-1]
#ttt = scenarioAB_Processing.get_criteria_scores(user_data, alternatives, "Days Inn")


opacity = 0.66
test_percents = []
for i in data:
    for x in i:
        test_percents.append(x)
    

# generate some multi-dimensional data & arbitrary labels
#data = 3 + 10* np.random.rand(segments, len(alternatives))

#percentages = (np.random.randint(5,20, (len(alternatives), segments)))

y_pos = np.arange(len(alternatives))


fig = plt.figure(figsize=(12,9))
fig.subplots_adjust(top=0.85)
ax = fig.add_subplot(111)

ax.xaxis.grid(True, linestyle='--', which='major',
                color='grey')
colors ='rgbcw'
patch_handles = []
left = np.zeros(len(alternatives)) # left alignment of data starts at zero

for i, d in enumerate(data):
    #print i
    
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
ax.set_xlabel('Total User Scores')


leg = ax.legend(loc="upper left", bbox_to_anchor=[0, 1.2],
        ncol=2, shadow=True, title="Legend", fancybox=True)

for label in ax.get_yticklabels():  # make the xtick labels pickable
    label.set_picker(True)
for lege in leg.get_texts():
    lege.set_picker(5)

def onpick(event):
    legline = event.artist
    #origline = spoke_labels[legline]

    if str(legline.get_text()) in users:
      print "yes"
      radio_user.main(alternatives, users, user_data, legline.get_text() )
    else:
      data = scenarioAB_Processing.get_criteria_scores(user_data, alternatives, legline.get_text())
      
      radio_test.main(data, alternatives, users, user_data, legline.get_text())

fig.canvas.mpl_connect('pick_event', onpick)

#vio_test.main(user_data)

plt.show()

