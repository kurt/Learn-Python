import numpy as np


#a = np.arrange(15).reshape(3,5)
a = np.array([2,3,4,5])
print(a)
print(a.shape)
print(a.ndim)
print(type(a))

b = np.array([[1,2],[3,4]])
print(b)


# complex
c = np.array([1,2,3], dtype = complex)
print(c)

#compatibility with C
d = np.dtype(np.int32)
print(d)

e = np.dtype(np.int8)
print(e)

# structured data
dt = np.dtype([('age',np.int8)]) 
print (dt)

 
dt = np.dtype([('age',np.int8)]) 
f = np.array([(10,),(20,),(30,)], dtype = dt) 
print(f)

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print (a['age'])

# c structure
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
print(student)

