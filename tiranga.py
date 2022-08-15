import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch


green = patch.Rectangle((0,1), width=12,height=2, facecolor ='green', edgecolor='grey')
white = patch.Rectangle((0,3), width=12,height=2, facecolor ='white', edgecolor='grey')
orange = patch.Rectangle((0,5), width=12,height=2, facecolor ='#FF6103', edgecolor='grey')

m,n = py.subplots()
n.add_patch(green)
n.add_patch(white)
n.add_patch(orange)

radius = 0.8
py.plot(6,4, marker = 'o', markerfacecolor = '#000088ff', markersize = 9.5)
chakra = py.Circle((6,4), radius, color = '#000088ff', fill = False, linewidth = 7)

for i in range(0,24):
    p = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
    q = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
    r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
    s = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)

    g = 6 + radius * np.cos(np.pi *i/12)
    h = 4 + radius * np.sin(np.pi *i/12)
    n.add_patch(patch.Polygon([[6,4],[p,r],[g,h],[q,s]],fill = True, closed = True, color = '#000088ff'))

py.axis('equal')
py.show()




