

file_handle = open("input_file.txt",'r')
print(file_handle)
for a in file_handle:
    print("another one")

#line counter - need to open again!!
count = 0
file_handle = open("input_file.txt",'r')
for line in file_handle:
	count = count + 1
print("Number of lines in file ", count)

# print a line you find 
file_handle = open("input_file.txt",'r')
for line in file_handle:
    if line.startswith("p"):
        print(line)
#file_handle.close()
print("-------------")

# print all lines that dont start with a space
file_handle = open("input_file.txt",'r')
for line in file_handle:
    if not line.startswith('from'):
        #print(line)
        print("do nothing atm")

#take from user input
fname = input("Enter the file name you want to open: ")
try:
    file_handle = open(fname)
except:
    print("File specified cannot be opened at this time")
    quit()
print("file opened successfully!")

   
        
