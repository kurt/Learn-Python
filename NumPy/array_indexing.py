import numpy as np

a = np.arange(10)
s = slice(2,7,2) # start, stop, step
print(a[s])

print(a[2:7:2]) #slice indexing

print(a[2:])
print(a[2:4])
print(a[2])

#indexing a two dimensional array
b = np.array([[1,2,3],[4,5,6]])

zero_col = b[...,0]
print(zero_col)
one_row = b[1,...]
print(one_row)

index = b[1,2]
print(index)

#indexing more advanced
c = b[[0,0,1],[1,1,2]]
print(c)

d = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

corners = np.array([[0,0,3,3],[0,2,0,2]]) 
print(d[[0,0,3,3],[0,2,0,2]])   


# boolean indexing
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
print (x[x > 5])

#iterating
a = np.arange(0,60,5)
a = a.reshape(3,4)
for i in np.nditer(a):
    print("Val of array is: ",i)

for i in np.nditer(a, order = 'C'):
    print("Val of array is: ",i)

for i in np.nditer(a, order = 'F'):
    print("Val of array is: ",i)

# iterate and manipulate

for x in np.nditer(a, op_flags = ['readwrite']):
    x[...]= 2*x
print("multiply by 2")    
print(a)






