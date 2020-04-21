class PrivateMethod:
    def __init__(self):
        self.__attr=1
    def __printhi(self):
        print("Hi")
    def printhello(self):
        print("Hello")

a=PrivateMethod()
a.printhello()
#a.__printhi() # these give errors because they are private
#a.__attr

class Person:
    def __init__(self, name, age):
        self.name=name
        self._age=age
    @property #getter
    def age(self):
        print("Retrieving {}s age".format(self.name))
        return self._age
    @age.setter
    def age(self, value):
        if type(value) is not int:
            raise TypeError("Age must be a number")
        if value < 0:
            raise ValueError("Age cant be negative")
        print("Setting {}s age to {}".format(self.name,value))
        self._age=value

adam=Person("Adam", 48)
ethan=Person("Ethan", 20)
adam.age
ethan.age
adam.age=50
ethan.age=21
