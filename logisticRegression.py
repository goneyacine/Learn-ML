import matplotlib.pyplot as plt
import csv
import numpy as np
import warnings
#training 
inputFile = csv.reader(open("train.csv"))
rows = []
y = np.array([0])
xs = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
for row in inputFile:
    rows.append(row)
    
rows.pop(0)
rows.pop(len(rows) - 1)


warnings.filterwarnings('ignore')

for row in rows:
    
    for i in range(15):
        if row[i] == "NA":
         row[i] = 0
    
    y = np.append(y,int(row[15]))
    x = np.array(
         [1,float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),
          float(row[8]),float(row[9]),float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14])])
    xs = np.vstack((xs,x))
    
    
    
theta = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])





for i in range(len(rows)):
   l = theta[0]
   for j in range(15):
       l += theta[j] * xs[i][j]
   h = 1 / (1 + np.exp(-l))
   f = (y[i] - h) * xs[i]
   for j in range(16):
       theta[j] += 0.1 * f[j]
        
        


print(theta)

#testing 

inputFile = csv.reader(open("test.csv"))
rows = []
y = np.array([0])
xs = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
for row in inputFile:
    rows.append(row)
    
rows.pop(0)
rows.pop(len(rows) - 1)

for row in rows:
    
    for i in range(15):
        if row[i] == "NA":
         row[i] = 0
    
    y = np.append(y,int(row[15]))
    x = np.array(
         [1,float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),
          float(row[8]),float(row[9]),float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14])])
    xs = np.vstack((xs,x))

errors = 0
for i in range(len(rows)):
    l = theta[0]
    for j in range(15):
        l += theta[j] * xs[i][j]
    l = 1 / (1 + np.exp(-l))
    if l < 0.5:
      l = 0
    else:
      l = 1
    if(y[i] != l):
      errors +=1 
      
print(errors / len(rows) * 100)
    




