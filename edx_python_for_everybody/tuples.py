t = tuple()
#sprint(dir(t))


(x,y) = (4, 'fred')
print (x, y)

d = {'a': 10 , 'b': 1 , 'c': 22}
d.items()
sorted(d.items())

for k,v in sorted(d.items()):
    print(k, v)

# sort by value
temp = list()
for k,v in sorted(d.items()):
    temp.append((v,k))

temp = sorted(temp)
print(temp)
