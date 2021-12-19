# Week2_assignment: Write a program usisng regular expression.

# Finding Numbers in a Haystack

# 1. Read through and parse a file with text and numbers:
# http://py4e-data.dr-chuck.net/regex_sum_1097714.txt
# (There are 76 values and the sum ends with 162)

# 2. Extract all the numbers in the file and compute the sum of the numbers.

# Data Format
# The file contains much of the text from the introduction of the textbook except
# that random numbers are inserted throughout the text.

# 3 The link open in a new window. Make sure to save the file into the same folder
# as you will be writing your Python program.

# Handling The Data
# The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers and summing up the integers.

# Sample data:
# http://py4e-data.dr-chuck.net/regex_sum_42.txt

# Actual data:
# http://py4e-data.dr-chuck.net/regex_sum_1097714.txt

fname = 'regex_sum_1097714.txt'     # string
fhandle = open(fname)                  # file
total = 0
import re
for line in fhandle:
    # print(line)
    x = re.findall('[0-9]+', line)
    # print(x)
    # Python, please iterate through x.
    # Take each element of x, assign it to the variable y, then execute the body of the for loop.
    for y in x:
        # print(y, type(y))
        z = int(y)
        total = total + z
print(total)


fname = 'regex_sum_1097714.txt'     # string
fhandle = open(fname)                  # file
total = 0
import re
for line in fhandle:
    # print(line)
    x = re.findall('[0-9]+', line)
    # print(x)
    # Python, please iterate through x.
    # Take each element of x, assign it to the variable y, then execute the body of the for loop.
    total = sum([int(y) for y in x]) + total
print(total)

total = 0
import re
for line in open('regex_sum_1097714.txt'):
    total = sum([int(y) for y in re.findall('[0-9]+', line)]) + total
print(total)

import re
print(sum([int(y) for y in re.findall('[0-9]+', open('regex_sum_1097714.txt').read())]))

import re
filename = 'regex_sum_1097714.txt'
content = open(filename).read()
numbers = [int(y) for y in re.findall('[0-9]+', content)]
total = sum(numbers)
print(total)

# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )


# Turn in Assignent
# Enter the sum from the actual data and your Python code below:

# Sum: 312162
# Python code:
