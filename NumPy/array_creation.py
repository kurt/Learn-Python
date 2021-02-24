import numpy as np

x = np.arange(10,20,2) #start at 10, go to up to 20 by 2
print(x)
y = np.linspace(5, 50, 10) # linspace 10 points between 5 and 50
print(y)
z = np.logspace(5,50,10) #logaritmic base 10
print(z)
a = np.logspace(5,50,10, base = 5) #logarithmic base 5 
print(a)
