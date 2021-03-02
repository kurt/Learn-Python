# assertions are not for error handling
# assertions are for our logic
# assertions should not have side effects - dont call something else
# optimizations are going to drop all of the assertions
# no silly assertions
# check a non-trivial property 
# make code fail proactively
# make code fail early
# assertions help assign blame
# documentation, assumptions, and postconditions 

a = 10
b =10
assert a ==10
assert b != 10
