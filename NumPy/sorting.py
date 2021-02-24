import numpy as np

# TO DO:
# lexsort : sort according to a key
# argmax() : max along a row or column
# where
# extract
# nonzero



a = np.array([[3,7],[9,1]]) 
print(np.sort(a))

dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt) 

print(np.sort(a, order = "name"))

# argsort:

x = np.array([3,1,2]) 

print ('Our array is:' )
print (x) 
print ('\n')   

print ('Applying argsort() to x:' )
y = np.argsort(x) 
print (y) 
print ('\n')   

print( 'Reconstruct original array in sorted order:' )
print (x[y]) 
print ('\n')  

print ('Reconstruct the original array using loop:' )
for i in y: 
   print (x[i]),




