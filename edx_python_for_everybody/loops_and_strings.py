


fruit = 'banana'
# for loop ----------------
for letter in fruit:
    print(letter)
print(fruit[0:4])
# while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print(fruit[:])
bob = 22
str1= "3232"

x = int(str1)
print(x+bob)

if 'a' in fruit:
    print('Found what I am looking for')
else:
    print("Just keep swimming")

#string manipulation
cap_fruit = fruit.upper()
print(cap_fruit)

# getting methods of string class
print("Fruit is a ",type(fruit))
print(dir(fruit))

pos = fruit.find("na")
print(pos)
pos2 = fruit.find("back")
print(pos2)

#replace 
cap_fruit = cap_fruit.replace("A","S")
print(cap_fruit)

