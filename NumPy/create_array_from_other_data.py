import numpy as np

#list to array
x = [1,2,3]
a = np.asarray(x)
print(a)

#list to array of floats
x = [1,2,3]
b = np.asarray(x, dtype = float)
print(b)

#tuple to array
x = (1,2,3)
c = np.asarray(x)
print(c)

#list of tuples
x=[(1,2,3),(4,5)]
d = np.asarray(x)
print(d)

#string
s = 'Hello World' 
e = np.fromstring(s, dtype = 'S1') 
e2 = np.fromstring(s, dtype = 'S1')
print(e)
print(e2)


# from iterable
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
f = np.fromiter(it, dtype = float) 
print(f)

