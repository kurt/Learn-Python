import numpy as np

#other array manipulation:
# reshape, flat, flatten (into one dimension), ravel(flatten basically)
# transpose, rollaxis, swapaxes
# broadcast, squeeze, expand_dims
# concatenate, stack, hstack, vstack
# split, hsplit, vsplit
# resize, append, insert, delete, unique


a = np.array([[1,2,3],[4,5,6]])
print(a.shape)

a.shape = (3,2)
print(a)
print(a.ndim)

# arranged data

b = np.arange(24, dtype = np.int8)
c = b.reshape(2,2,6)
print(c)

# data size in bytes
print("Size of an int: ", b.itemsize)
x = np.array([1,2,3,4,5], dtype = np.float32)
print("Size of a float: ", x.itemsize)
print(x.flags)

# create empty array
d = np.empty([2,2],dtype = int)
print(d)
# create array of zeros
e = np.zeros([2,2], dtype = int)
print(e)
#custom data type
f = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')]) 
print(f)
# ones array
g = np.ones(5) 
print(g)

#transpose
a = np.arange(0,60,5)
a = a.reshape(3,4)
Aprime = a.T
print("a transposed")
print(Aprime)
