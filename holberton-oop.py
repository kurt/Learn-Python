class Dog:
   def  __init__(self, name, height, weight):
       self.name = name
       self.height = height
       self.weight = weight
   def eat(self):
       print("{} is eating".format(self.name))
   def walk(self):
       print("{} is walking".format(self.name))
   def sleep(self):
       print("{} is now asleep ZZzzZ".format(self.name))

max = Dog("max", 70, 40)
charlie = Dog("charlie", 50, 20)
max.eat()
charlie.sleep()
max.walk()
