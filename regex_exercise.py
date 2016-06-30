# The basic outline of this problem is to read the file,
# look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+'
# and then converting the extracted strings to integers
# and summing up the integers.

import re

# open file correctly
fname = raw_input('Please enter file name:')
try:
    fhandler = open(fname)
except:
    print 'bad name!'
    quit

# find numbers in file
lon_str = []
for line in fhandler:
    lon_str= lon_str + re.findall('[0-9]+',line)

# now I have a list of strings, go through list to convert each to numbers and sum them
sum = 0
for num_str in lon_str:
    num_str = int(num_str)
    sum = sum + num_str

print sum
    
    