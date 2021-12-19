# 9.4 Write a program to read through the mbox-short.txt and figure out
# who has sent the greatest number of mail messages.
## The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail.
## The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
## After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

fname = input("Enter file:")
#fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

dict_maila = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    e_lines = line.split()
    #print(e_lines)
    e_adress = e_lines[1]
    #print(e_adresses)

    # idiom: retreive/create/update counter
    dict_maila[e_adress] = dict_maila.get(e_adress, 0) + 1
    #print(e_adress, 'new', dict_maila[e_adress])

#print(dict_maila)

# find who has sent the greatest number of mail messages
largest = -1
themaila = None
for k,v in dict_maila.items():
     #print(k,v)
     if v > largest:
        largest = v
        themaila = k # capture & remember the key that was largest

print(themaila, largest)
