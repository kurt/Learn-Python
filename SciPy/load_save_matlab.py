import scipy
import scipy.io as sio
import numpy as np


vect = np.arange(10)
sio.savemat("Data/array.mat",{'vect':vect})


data_in = sio.loadmat("Data/array.mat")
print(data_in)
print(data_in['vect'])
newdata = data_in['vect']
print(newdata[0][3])
print(newdata.flatten())




