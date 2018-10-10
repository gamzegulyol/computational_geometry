
# coding: utf-8

# In[5]:




# In[6]:




# In[11]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])

point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])



# In[12]:

d1=-np.sum(point1*normal1)
d2=-np.sum(point2*normal2)
d3=-np.sum(point3*normal3)
d1,d2,d3


# In[13]:

#4x+5y+6z+7  -<4,5,6>.<x,y,z> aradaki işlem
xx, yy = np.meshgrid(range(5),range(5))


# In[14]:

z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color='magenta')


# In[18]:


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
n=100
theta_max = 8*np.pi
theta = np.linspace(0,theta_max,n)
x=np.sin(theta)
y=np.cos(theta)
z=theta
ax.plot(x,y,z, 'b', lw=2)


# In[ ]:



