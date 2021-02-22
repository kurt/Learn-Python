
friends = ["joseph", "Tim", "Steve"]

nums = [1 , 4, 5]

list_of_list= [friends, nums]


for i in nums:
    print(i)

print(friends[2])
nums[2] = 10
print(nums)
print("Length of nums is ", len(nums))
print(range(4))

# concatenation of lists
new = friends + nums
print(new)

# addin things to list
nums.append(12)
print(nums)

# see if in
print( 9 in nums)
print(10 not in nums)

# sort
nums.append(3)
old_nums = nums
print(old_nums)
nums.sort()
print(nums)
print(old_nums)


# max, min, sum,

print(sum(nums))
print(min(nums))
print(max(nums))

#### strings 
abc = "String with three words"
stuff = abc.split()
for i in stuff:
    print(i)
print("-------")
for i in range(4):
    print(stuff[i])

# array like lists
a = [[1, 2, 3], [4, 5, 6]]
print(a[0][1])
print(a[1][2])





