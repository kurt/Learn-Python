


class Parent:
    def __init__(self):
        print("calling parent constructor")
    def parentMethod(self):
        print("Parent Method")
    def methodToOverride(self):
        print(10)


class Child (Parent):
    def __init__(self, name):
        print("calling child constructor")
        self.name = name
    def methodToOverride(self):
        print(20)


child = Child("Tommy")
child.methodToOverride()
child.parentMethod()

# checking if subclass
print("Is Child a sub of Parent? ", issubclass(Child,Parent))

print("Is child a Child object? ", isinstance(child, Child))
