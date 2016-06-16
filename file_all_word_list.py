#8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method. The program should build
# a list of words. For each word on each line check to
# see if the word is already in the list and if not
# append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

# open file:
file_name = raw_input('Enter a file name please: ')
try:
    handler = open(file_name)
except:
    print 'Bad file name! I am outta the game!'
    quit()
    
# build list of words:
low = []

# read line
for line in handler:
    # split the line I am on
    low_line = line.split()
    
    # test splitting
    # print low_line
    
    for word in low_line:
    
        #test word splitting
        # print word
        
        # check if word is in list of words, if not, add it in
        if word not in low:
            low.append(word)
            
            # test appending
            # print low

# sort and print
low.sort()
print low