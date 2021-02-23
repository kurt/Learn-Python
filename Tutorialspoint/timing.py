import time

ticks = time.time()


# do something - open a file
name = input('Enter file to parse:')
file_handle = open(name)

tick2 = time.time()

print("Time to select and open file: ",tick2 - ticks)
print (time.localtime());
