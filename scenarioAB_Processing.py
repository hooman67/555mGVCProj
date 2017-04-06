import xml.etree.ElementTree as ET
'''tree = ET.parse('ScenarioA-Hotel.xml')
root = tree.getroot()'''


users = []
weights = []
scores = []
def get_user_data(xml_name):
  tree = ET.parse(xml_name)
  root = tree.getroot()
  total = []
  for i in root.findall('Users'):
    for x in i.findall('User'):
      temp = []
      temp.append(x.get('name'))
      for y in x.findall('Weights'):
        temp_weights = {}
        for a in y.findall('Weight'):
          temp_weights.update({a.get('objective'): a.get('value')})
      temp.append(temp_weights)
      for z in x.findall('ScoreFunctions'):
        t = {}
        for sf in z.findall('ScoreFunction'):
          t1 = {}
          for score in sf.findall('Score'):
            t1.update({score.get('domain-element'): score.get('value')})
          t.update({sf.get('objective'): t1})
      temp.append(t)
      total.append(temp)
    
    return total
    

def get_alt_data(xml_name):
  tree = ET.parse(xml_name)
  root = tree.getroot()
  alts = {}
  for a in root.findall('ChartStructure'):
    for i in a.findall('Alternatives'):
      for x in i.findall('Alternative'):
        temp_vals = {}
        for z in x.findall('AlternativeValue'):
          temp_vals[z.get('objective')] = z.get('value')
        alts[x.get('name')] = temp_vals
  return alts

  

def get_total_values(total, alts):
  tv = []
  for i in range(len(total)):
    tv_temp = []
    for z in alts.iterkeys():
      total_score = 0
      for x in total[i][2].iterkeys():
        val = alts[z][x] #so this is like highway, downtown, highspeed, lowspeed
        print val
        total_score += (float(total[i][2][x][val]) * float(total[i][1][x]))
      tv_temp.append(total_score)
    tv.append(tv_temp)
  return tv
'''
def get_criteria_scores(total, alts, alt_name):
  tv = []
  for i in range(len(total)):
    #tv_temp = []
    for z in alts[alt_name].iterkeys(): #for one alternative, ie basement, iterate critera ie internet
      tv_temp = []
      for x in total[i][2].iterkeys(): #for score functions on critera
        val = alts[alt_name][z] #so this is like highway, downtown, highspeed, lowspeed
        print x
        print val
        print total[i][2][x][val]
        total_score = float(total[i][2][x][val]) * float(total[i][1][x])
        tv_temp.append(total_score)
    tv.append(tv_temp)
  return tv ''' 

def get_criteria_scores(total, alts, alt_name):
  tv = []
  for i in range(len(total)):
    tv_temp = []
    for x in total[i][2].iterkeys(): #for score functions on critera
      val = alts[alt_name][x] #so this is like highway, downtown, highspeed, lowspeed
      total_score = float(total[i][2][x][val]) * float(total[i][1][x])
      tv_temp.append(total_score)
    tv.append(tv_temp)
  return tv

def get_criteria_scores_one_user_multi_alts(total, alts, user_name):
  tv = []
  for i in range(len(total)):
    if total[i][0] == user_name:
      for y in alts.iterkeys():
        tv_temp = []
        for x in total[i][2].iterkeys(): #for score functions on critera
          val = alts[y][x] #so this is like highway, downtown, highspeed, lowspeed
          total_score = float(total[i][2][x][val]) * float(total[i][1][x])
          tv_temp.append(total_score)
        tv.append(tv_temp)
  print tv
  return tv

def get_single_criteria_scores(total, alts, alt_name, criteria_name):
  tv = []
  for i in range(len(total)):
    #for x in total[i][2].iterkeys(): #for score functions on critera
    val = alts[alt_name][criteria_name] #so this is like highway, downtown, highspeed, lowspeed
    total_score = float(total[i][2][criteria_name][val]) * float(total[i][1][criteria_name])
    tv.append(total_score)
  return tv


      









