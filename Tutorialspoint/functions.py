


def changearray( mylist ):
    print("In func before change: ", mylist)
    mylist[2]=50
    print("In func after change: ", mylist)

def changearray2(mylist):
    mylist = [1,2,3,4] 
    print("In func2 after change: ", mylist)


mylist = [10,30,30]
changearray(mylist)
print("My list outside func: ", mylist)

changearray2(mylist)
print("My list outside func2: ", mylist)

# anonymous functions
sum = lambda arg1, arg2: arg1 + arg2 #an anonymous function

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
