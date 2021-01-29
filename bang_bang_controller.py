# bang_bang_controller.py
import numpy as np
import scipy as sp
from scipy import integrate
from matplotlib import pyplot as plt

def dxdt(t,x):
    global c  
    if x[0] < 0:
        u=2
    else:
        u=-2
    d=np.array([x[1],u])
    c=c+1
    return d

x0=np.array([-10,0])
global c
c=0;
timef=10;

#sol=sp.integrate.solve_ivp(dxdt,[0,timef],x0);
#print(sol.y)
#plt.title("Bang-Band Phase Portrait")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.plot(sol.y[0,:],sol.y[1,:])
#plt.show()

for i in range(1,20):
   sol=sp.integrate.solve_ivp(dxdt,[0,timef],x0);
   plt.title("Bang-Band Phase Portrait")
   plt.xlabel("x")
   plt.ylabel("y")
   plt.plot(sol.y[0,:],sol.y[1,:])
   x0=x0+1
plt.show()
