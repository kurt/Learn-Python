# also known as associative array
# a database - there are keys to each item

purse = dict()
purse['money'] = 12 # dictname['key'] = value
purse['tissues'] = 75
purse['candy'] = 3

print(purse['candy'])

purse['candy']= purse['candy'] + 2
print(purse['candy'])
print(purse)

# initialize a dictionary
new_dict = {'gun': 'winchester', 'value': 3800, 'owner': 'Steve'}
print(new_dict['owner'])


# Read some data
name_tally = dict()
names = ['Tim', 'Bob', 'Steve', 'Bob', 'Steve', 'Francis'] 
#   = input("")
for name in names:
    if name not in name_tally:
        name_tally[name] = 1
    else:
        name_tally[name] = name_tally[name]+1
print(name_tally)  

# get method
x = name_tally.get('Tim',0)
print(x)
x = name_tally.get('Steve',0)
print(x)

