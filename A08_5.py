# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the second word
# in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

# setup counter:
count = 0


# open file:
fname = raw_input('Please enter file name: ')
try:
    fhandler = open(fname)
except:
    print 'What did I say? You did not listen! Bye!'
    quit()


# go through lines to find ones start with From
for line in fhandler:

    # for each line, split them into low, print out second word, update counter
    if line.startswith('From: '):
        low = line.split()
        print low[1]
        count = count+1

# print count result
print "There were", count, "lines in the file with From as the first word"
