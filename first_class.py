class Dog:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def eat(self):
        print("{} is eating".format(self.name))

max=Dog("Steve", 70, 40)
max.eat()
print("Here")
