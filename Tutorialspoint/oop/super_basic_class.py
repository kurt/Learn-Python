class super_basic_class:
    'This is the documentation for super_basic_class'
    BCcount = 0
    BCval = 0




#sbc = super_basic_class() #object instantiation
print("Initial BCcount: ",super_basic_class.BCcount)
super_basic_class.BCcount = 10
print("Updated BCcount: ",super_basic_class.BCcount)

print(dir(super_basic_class))
print ("Documentation", super_basic_class.__doc__)
print ("super_basic_class.__name__:", super_basic_class.__name__)
print ("super_basic_class.__module__:", super_basic_class.__module__)
print ("super_basic_class.__bases__:", super_basic_class.__bases__)
print ("super_basic_class.__dict__:", super_basic_class.__dict__ )

