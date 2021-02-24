import numpy as np 

#save and load text
a = np.array([1,2,3,4,5]) 
np.savetxt('Data/out.txt',a) 
b = np.loadtxt('Data/out.txt') 
print (b)

#save and load data
x = np.array([1,2,3,4,5])
np.save("Data/outfile",a)
y = np.load("Data/outfile.npy")
print(y)
