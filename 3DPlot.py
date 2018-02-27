from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import csv

x = []
y = []
z = []
labels = []

with open('data.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        #print(row)
        a,b,c,d = row[0].split(',')
        #print(a,b,c,d)
        x.append(float(a))
        y.append(float(b))
        z.append(float(c))
        # d = label, can use for colormap
        if int(d):
            labels.append('r')
        else:
            labels.append('b')

#print(labels)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for a,b,c,d in zip(x,y,z,labels):
    ax.scatter(a,b,c,c=d)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
