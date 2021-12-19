fname = input('Enter File: ')
# fname = 'intro.txt'
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

#print(dict_fname)

temp = list()
for k,v in dict_fname.items():
    # print(k,v)
    new_tuple = (v,k)
    temp.append(new_tuple)

# print('Flipped', temp)
temp = sorted(temp, reverse = True)
# print('Sorted', temp[:5])

for v,k in temp[:5]:
    print(k,v)





# x = sorted(dict_fname.items())
# print(x[:5]) # sorted based on key
