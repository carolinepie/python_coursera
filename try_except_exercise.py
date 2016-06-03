#write a pay computation to give employee 1.5 times
#hourly rate for overtime, if they have worked above
# 40 hours, consider case of bad inputs

hrs_str = raw_input("Enter hours worked: ")
rate_str = raw_input("Enter original rate:")
wage = 0

#deal with hours bad input, only 1 attempt allowed
try:
    hrs = float(hrs_str)
except:
    print "please enter number!"
    quit()

#deal with rate bad input, 1 attempt only
try:
    rate=float(rate_str)
except:
    print "please enter number!"
    quit()
    
if hrs <= 40:
    wage = hrs*rate

else:
    wage = 40*rate+(hrs-40)*1.5*rate
    
print 'Pay:',wage