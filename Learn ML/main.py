import matplotlib.pyplot as plt
import csv
import numpy as np

#import data

inputFile = csv.reader(open("dataset.csv"))
rows = []
y = np.array([0])
xs = np.array([[0,0,0]])
for row in inputFile:
    rows.append(row)
    
rows.pop(0)
rows.pop(len(rows) - 1)

rooms = [0]
spaces = [0]
prices = [0]




for row in rows:
    if row[0] == "NA" or row[3] == "NA" or row[4] == "NA":
     continue
    else:
     y = np.append(y,int(row[0]))
     x = np.array([1,int(row[3]),int(row[4])])
     xs = np.vstack((xs,x))
    rooms.append(int(row[4]))
    prices.append(int(row[0]))
    spaces.append(int(row[3]))
theta = [0,0,0]
cost = 0
for i in range(len(xs)):
    cost+= pow(theta[0] + theta[1] * xs[i][1] + theta[2] * xs[i][2] - y[i],2) / 2

print("cost before == " + str(cost))

theta = np.linalg.inv(xs.T.dot(xs)).dot(xs.T).dot(y)

cost = 0
for i in range(len(xs)):
    cost+= pow(theta[0] + theta[1] * xs[i][1] + theta[2] * xs[i][2] - y[i],2) / 2

print("cost after == " + str(cost))

print(theta)



   
#display data
plt.style.use('_mpl-gallery')

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(spaces,rooms,prices)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

x_ = np.linspace(0, 30, 100)
y_ = np.linspace(0, 100, 100)
x_, y_ = np.meshgrid(x_, y_)

# Compute z values using the plane equation
z = theta[0] + theta[1] * x_ + theta[2] * y_
ax.plot_surface(x_, y_, z, cmap='viridis')


plt.show()

