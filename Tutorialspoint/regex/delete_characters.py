import re

phone = "2004-595-559 #this is a phone number"
email = "stewart.kurt2@gmail.com"

num = re.sub(r"#", "", phone) # delete the '#'
print(num)

num = re.sub(r"\D", "", phone) #delete all non digits
print(num)

num = re.sub(r'#.*$', "", phone) # delete everything from "#" on
print(num)

user_name = re.sub(r"@.*$", "", email)
print(user_name)
