

name = input('Enter file to parse:')
file_handle = open(name)
#text = file_handle.read()

counts = dict()


#for char in '-.,':
 #   text=text.replace(char,' ')
#text = text.lower()
#print(text)


for line in file_handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#print('Counts ', counts)

common_count = None
common_word = None
for word,count in counts.items():
    if common_count is None or count > common_count:
        common_word = word
        common_count = count

print(common_word, ": ", common_count)
#for key in counts:
    #print(key, counts[key])
