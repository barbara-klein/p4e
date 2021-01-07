# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list
# and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Initial code from Autograder:
fname = input("Enter file name: ")
#fname = 'romeo.txt'
fh = open(fname)
outcome_words = list()

def is_word_in(words, word):
    return outcome_words.count(word) > 0

for line in fh:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for word in words:

        #print(x)
        if is_word_in(outcome_words, word) == False:
            outcome_words.append(word)
outcome_words.sort()
print(outcome_words)

#or:
#fname = input("Enter file name: ")
#fh = open(fname)
#outcome_words = list()
#for line in fh:
#    line = line.rstrip()
#    words = line.split()
#    for word in words:
#        x = outcome_words.count(word)
#        if x == 0 :
#            outcome_words.append(word)
#outcome_words.sort()
#print(outcome_words)
