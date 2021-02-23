import re 
pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3" # raw string of group 1,2,3 of (\d)
second_pattern = r"\1 \2 \3"
third_pattern = r"(\1) \2 \3"
print("Enter a phone number: ")
user_input = input()

print(re.sub(pattern,new_pattern, user_input))
print(re.sub(pattern,second_pattern, user_input))
print(re.sub(pattern,third_pattern, user_input))
