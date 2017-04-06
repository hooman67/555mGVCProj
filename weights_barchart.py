from pylab import *
import scenarioAB_Processing
def draw_bar(user_data, alts, crit_name, name_of_alt, users):
  #figure(figsize=(9, 9))

  pos = arange(len(users))+.5    # the bar centers on the y axis
  pool = [0, 0, 30, 61]
  internet = [80, 0, 30, 11]
  location = [20, 100, 40, 27]

  criteria = scenarioAB_Processing.get_single_criteria_scores(user_data, alts, name_of_alt, crit_name)
  for i in range(len(criteria)):
      criteria[i] = int(criteria[i] * 100)

  weights = []
  for i in range(len(user_data)):
      temp_weights = []
      weights.append(int(float(user_data[i][1][crit_name])*100))

  figure(111)

  barh(pos, criteria, align='center')
  barh(pos, weights, align='center', fill=False)
  yticks(pos, users)
  xlabel('Weights')
  
  grid(True)

  plt.show()
