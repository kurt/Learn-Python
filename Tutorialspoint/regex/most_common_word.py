import re
#name = input('Enter file to parse:')
file_handle = open("file_to_count.txt")
#print(dir(file_handle))
text = file_handle.read()
new_text = re.sub(r"[^a-zA-Z]", " ", text)
list1 = re.findall(r"\w+",new_text)

counts = dict()
 
for word in list1:
    counts[word] = counts.get(word,0) + 1

#print('Counts ', counts)

common_count = None
common_word = None
for word,count in counts.items():
    if common_count is None or count > common_count:
        common_word = word
        common_count = count

print("The most common word is: '", common_word, "' it appears: ", common_count, "times")
