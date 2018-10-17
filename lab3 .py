
# coding: utf-8

# In[54]:

def draw_my_line(normal_vector, point_on_line):
    a=normal_vector[0]
    b=normal_vector[1]
    c=normal_vector[2]
    
    x_0=point_on_line[0]
    y_0=point_on_line[1]
    z_0=point_on_line[2]
    x=[]
    y=[]
    z=[]
    x.append(other_point[0])
    y.append(other_point[1])
    z.append(other_point[2])
    
    for t in range(-1,10):
        x.append(x_0+t*a)
        y.append(y_0+t*b)
        z.append(z_0+t*c)
    return (x,y,z)


# In[55]:

def my_scalar_product(a,b):
#a=[-1,2,4]
#b=[-4,-5,2]
#a transpose b?
    a_t_b=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return a_t_b


# In[56]:

def point_on_line(normal_vector, point_on_line,other_point):
    
    a_x=other_point[0]-point_on_line[0] #otherpoint pointOnLine ikilisi
    a_y=other_point[1]-point_on_line[1]
    a_z=other_point[2]-point_on_line[2]
    
    b=[a_x,a_y,a_z]
    a=normal_vector
    
    c=my_scalar_product(a,b)/my_scalar_product(a,a)
    
    b_x=c*a[0]
    b_y=c*a[1]
    b_z=c*a[2]
    
    nearest_point_on_line=[b_x,b_y,b_z]
    
    return nearest_point_on_line


# In[57]:

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib notebook')
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
p=(0,0,0)              #hattı tanımlayan iki parametre
n=(1,1,1)           #bekleme noktası
other_point=[1,2,7]
n_p=point_on_line(n,p,other_point)
#n_p değeri hat üzerindeki bize en yakın nokta

points=draw_my_line(n,p)
ax = plt.axes( projection='3d')
ax.plot3D(points[0],points[1],points[2],"magenta")
ax.scatter(other_point[0],other_point[1],other_point[2],"blue")
ax.scatter(n_p[0],n_p[1],n_p[2],"red")

plt.show()


# In[6]:

#matplotlib notebook
plt.plot(points[0],points[1],points[2])


# In[ ]:



