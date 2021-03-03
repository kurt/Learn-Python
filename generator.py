

# basic generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

# generator object
x = simpleGeneratorFun()
print("Generator Object")
print(x.__next__())
print(x.__next__())
print(x.__next__())
