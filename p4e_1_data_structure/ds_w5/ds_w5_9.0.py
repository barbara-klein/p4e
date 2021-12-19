fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

dict_fname = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # idiom: retreive/create/update counter
        dict_fname[word] = dict_fname.get(word, 0) + 1
        # print(word, 'new', dict_intro[word])

# print(dict_fname)

# find the most common words
largest = -1
theword = None
for k,v in dict_fname.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k # capture/remember the key that was largest

#print('Done', theword, largest)
print(theword, largest)
