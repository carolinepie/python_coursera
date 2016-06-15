# Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
#     X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point
# values from each of the lines and compute the average
# of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

file_name_with_space = raw_input("Enter a file name: ")
file_name = file_name_with_space.strip()
average = 0
count = 0

try:
    handler = open(file_name)
except:
    print 'Bad file name input! Bye!'
    quit()

for line in handler:
    if line.startswith("X-DSPAM-Confidence:"):
        start_pos = line.find(' ')
        num_str_with_space = line[start_pos:]
        num_str = num_str_with_space.strip()
        num = float(num_str)
        average = (average * count + num) / (count + 1)
        count = count + 1

print 'Average spam confidence:',average