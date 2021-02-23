import re

line = "Cats are smarter than dogs"
three_lines =" Cats are dogs \n dogs are dogs \n phil is a dog" 

searchObj = re.search(r"dogs", line, re.M|re.I) # ignore case and multiline
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
   print("At least one dog found!!")
   print(dir(searchObj))
   #print ("NUmber of dogs found: ",len(searchObj))
else:
   print ("Nothing found!!")

print ("The number of dogs in string: " ,len(re.findall(r"dogs", line, re.M|re.I)))

print ("The number of dogs in three lines: " ,len(re.findall(r"dogs", three_lines, re.M|re.I)))
