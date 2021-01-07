# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

str = "X-DSPAM-Confidence:    0.8475";
col_pos = str.find(':')
#print(col_pos)
piece = str[col_pos+5:]
#print(piece)
#print(piece+42.0) # will fail since pieace is a str
value = float(piece)
print(value)
#print(value+42.0)

Autograder:
text = "X-DSPAM-Confidence:    0.8475";
col_pos = text.find(':')
piece = text[col_pos+5:]
value = float(piece)
print(value)
