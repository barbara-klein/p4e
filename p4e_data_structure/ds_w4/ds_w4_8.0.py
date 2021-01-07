han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian in a compound statement:
    if len(wds) < 3 or wds[0] != "From" :
        continue
    print(wds[2])


#for line in han:
    #line = line.rstrip()
    #print('Line:', line)
    # Guaridan 1 for empty list
    #if line == '' :
        #print('Skip Blank')
        #continue
    #wds = line.split()
    #print('Words:',wds)
    # Guardian 2
    #if len(wds) < 3 :
        #continue
    #if wds[0] != "From" :
        #print('Ignore')
        #continue
    #print(wds[2])
