# basic_plotting.py
import numpy as np 
from matplotlib import pyplot as plt

x=np.arange(1,22)
y= 2*x+5

plt.title("Matplotlib basic plot")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()

