import numpy as np

a = np.arange(6)

print("our array",a)

print(id(a))

# No Copy?
b = a
print(id(b))
#View/shallow copy
c=a.view()
print(id(c))
#deep copy
d=a.copy()

#Manipulation
b.shape = (3,2)

# Results
print("No Copy")
print(a)
print("View")
print(c)
print("Deep Copy")
print(d)




