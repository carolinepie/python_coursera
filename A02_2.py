#write a pay computation to give employee 1.5 times
#hourly rate for overtime, if they have worked above
# 40 hours, do not consider case of bad inputs

def computepay(hrs, rate):
    if (hrs > 40):
        return 40*rate+1.5*(hrs-40)*rate
    else:
        return float(rate)*float(hrs)
        
hrs_str = raw_input("input hours please: ")
rate_str = raw_input("input rate please: ")

hrs = float(hrs_str)
rate = float(rate_str)

print "Pay",computepay(hrs, rate)
