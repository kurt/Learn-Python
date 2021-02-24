import numpy.matlib
import numpy as np

# TO DO:
#vdot - vector dot
#inner - inner product
#inv


# empty array 

print (np.matlib.empty((2,2)) )

# empty zeros
print (np.matlib.zeros((2,2)) )

# Identity
print (np.matlib.identity(5, dtype = float))

#dot product
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
dproduct = np.dot(a,b)
print(dproduct)

# solve linear equations
A = np.array([[1, 2], [3, 5]])
B = np.array([1, 2])
x = np.linalg.solve(A,B)
print(x)

#determinant
c = np.array([[1,2],[3,4]])
print(np.linalg.det(a))

#matmul - matrix product
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print (np.matmul(a,b))
