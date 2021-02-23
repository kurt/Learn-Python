class myVector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" %(self.a, self.b)

    def __add__(self,other):
        return myVector(self.a + other.a, self.b + other.b)

mv1=myVector(3,14)
mv2=myVector(4,-10)
print(mv1 + mv2)

