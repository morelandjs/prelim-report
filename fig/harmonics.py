#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
xx, yy = np.meshgrid(x,y)

# second harmonic
#e2 = np.exp(-(xx**2+yy**2)*(1+0.2*np.cos(2*(np.arctan2(yy,xx))))**2/6)
#e2[e2<0.1] = None
#fig = plt.contourf(x,y,e2,cmap=plt.cm.Blues,extend="both")
#fig.cmap.set_under('w')
#fig.set_clim(0.1, 1)
#plt.axis('equal')
#plt.axis('off')
#plt.savefig("e2.pdf")

# third harmonic
#e3 = np.exp(-(xx**2+yy**2)*(1+0.2*np.cos(3*(np.arctan2(yy,xx)-np.pi/6)))**2/6)
#e3[e3<0.1] = None
#fig = plt.contourf(x,y,e3,cmap=plt.cm.Blues,extend="both")
#fig.cmap.set_under('w')
#fig.set_clim(0.1, 1)
#plt.axis('equal')
#plt.axis('off')
#plt.savefig("e3.pdf")

# fourth harmonic
#e4 = np.exp(-(xx**2+yy**2)*(1+0.2*np.cos(4*(np.arctan2(yy,xx))))**2/6)
#e4[e4<0.1] = None
#fig = plt.contourf(x,y,e4,cmap=plt.cm.Blues,extend="both")
#fig.cmap.set_under('w')
#fig.set_clim(0.1, 1)
#plt.axis('equal')
#plt.axis('off')
#plt.savefig("e4.pdf")


# fifth harmonic
e5 = np.exp(-(xx**2+yy**2)*(1+0.2*np.cos(5*(np.arctan2(yy,xx)+np.pi/10)))**2/6)
e5[e5<0.1] = None
fig = plt.contourf(x,y,e5,cmap=plt.cm.Blues,extend="both")
fig.cmap.set_under('w')
fig.set_clim(0.1, 1)
plt.axis('equal')
plt.axis('off')
plt.savefig("e5.pdf")






