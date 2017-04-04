from pylab import *
def draw_bar(criteria):
  #figure(figsize=(9, 9))
  val = 3+10*rand(4)    # the bar lengths
  pos = arange(4)+.5    # the bar centers on the y axis
  pool = [0, 0, 30, 61]
  internet = [80, 0, 30, 11]
  location = [20, 100, 40, 27]
  if criteria == 'Pool':
      val = pool
      #title('Criteria: Pool')
  elif criteria == 'Internet':
      val = internet
      #title('Criteria: Internet')
  else:
      val = location
      #title('Criteria: Location')

  figure(111)
  barh(pos,val, align='center')
  yticks(pos, ('Ann', 'Bob', 'Carol', 'Emily'))
  xlabel('Weights')
  
  grid(True)

  plt.show()
