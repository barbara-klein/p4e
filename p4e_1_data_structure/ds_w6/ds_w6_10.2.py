# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.


# name = input("Enter file:")
fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)

dict_fname = dict()
for line in handle:
    if not line.startswith('From ') : continue
    e_lines = line.split()
    # print(e_lines[5])
    hour, min, sec = e_lines[5].split(':')
    # print(hour)

    dict_fname[hour] = dict_fname.get(hour, 0) + 1
    # print(hour, dict_fname[hour])

# print(dict_fname)

# x = sorted(dict_fname.items())
# print(x)

for k,v in sorted(dict_fname.items()):
    print(k,v)
