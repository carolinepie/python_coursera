# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the
# string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour.


# open file and check whether it is okay
fname = raw_input('Enter file name please: ')
try:
    fhandler = open(fname)
except:
    print 'Bad file name! Bye.'
    quit()

# create empty dict
dohr = dict()

# in file:

# extract line startwith.('From: ')
for line in fhandler:
    if line.startswith('From '):
        # split into low;
        low = line.split()
        # extract time
        time = low[5]
        # split time
        lot = time.split(':')
        # extract hour
        hr = lot[0]
        # find hour in dict and increase its counts
        dohr[hr] = dohr.get(hr,0)+1
        
        
# create tupple list
tups = dohr.items()

# sort tupple list
sorted_tups = sorted(tups)

# print hour,counts
for hr,count in sorted_tups:
    print hr,count