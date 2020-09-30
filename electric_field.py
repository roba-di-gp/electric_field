import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

plt.rcParams['image.cmap'] = 'jet'
plt.rcParams['axes.facecolor'] = 'k'

#charges values and positions
qs =   ([1,-0.5,0],
        [1,0.5,0],
        [-1,0,-0.5],
        [-1,0,0.5])

#n^2 points will be plotted
n = 20

xlim, ylim = 1,1
a = np.linspace(-xlim,xlim,n)
b = np.linspace(-ylim,ylim,n)
x, y = np.meshgrid(a,b)

#electric field vectors
def e(q,x,y):
    den = (np.hypot(x-q[1],y-q[2]))**3
    return q[0]*(x-q[1])/den, q[0]*(y-q[2])/den

#color vectors
def color(q,x,y):
    den = np.hypot(x-q[1],y-q[2])
    return q[0]*(x-q[1])/den, q[0]*(y-q[2])/den

Ex = Ey = xcolor = ycolor = np.zeros((n,n))

for q in qs:
    ex, ey = e(q, x, y)
    Ex = np.add(Ex,ex)
    Ey = np.add(Ey,ey)
    xcolor = np.add(xcolor,color(q,x,y)[0])
    ycolor = np.add(ycolor,color(q,x,y)[1])

#vector field plot
plt.figure(1,(5,5))
ax1 = plt.subplot(111)

color = np.hypot(xcolor,ycolor)
u, v = Ex/np.hypot(Ex,Ey), Ey/np.hypot(Ex,Ey)

plt.quiver(x,y,u,v,color,zorder=2)
plt.grid(alpha=0.2)

#plotting charges
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q in qs:
    pos = (q[1],q[2])
    ax1.add_artist(Circle(pos, 0.02, color=charge_colors[q[0]>0],zorder=4))

#field lines plot
plt.figure(2,(5,5))
ax2 = plt.subplot(111)

plt.xlim(-xlim,xlim)
plt.ylim(-ylim,ylim)

#plotting charges
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q in qs:
    pos = (q[1],q[2])
    ax2.add_artist(Circle(pos,0.02,color=charge_colors[q[0]>0],zorder=4))

plt.streamplot(x, y, Ex, Ey, color=color, linewidth=0.5, density=2, arrowstyle='->', arrowsize=1.5)

plt.show()

plt.rcParams.update(plt.rcParamsDefault)


