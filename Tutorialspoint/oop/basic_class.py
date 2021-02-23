class basic_class:
    'This is the documentation for basic_class'
    BCcount = 0
    BCval = 0

    def __init__(self):
        print("Constructor Called")
        self.count = 1
        self.val = 10
    def __del__(self):
        print("Destructor Called")
    def computeVal(self):
        val = 10/2
    def printCount(self):
        print(self.count)
    def printBCCount(self):
        print(basic_class.BCcount)
# end of class definition


bc = basic_class() #object instantiation
bc.printCount()
bc.printBCCount()
bc.computeVal()
# get, set, has, del
print(getattr(bc, 'val'))
print("Does it have a steeple? ",hasattr(bc, 'steeple'))
setattr(bc, 'val', 22)
print(getattr(bc, 'val'))
delattr(bc, 'val')
print("Does it have a val? ",hasattr(bc, 'val'))
del bc
