months = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
    }

totalDays = 0
dateCounter = 6 #the first sunday in Jan 1901 is the 6th

for y in range(1901, 2001):
    if (y%4 == 0 and y != 1900):
        leap = True
    else:
        leap = False
    print ("Year: " + str(y))
    #One Year
    for x in range (1, 13):        
        days = months[x]

        if (x == 2 and leap):
            days += 1
        #print ("Month: " + str(days))

        while (dateCounter <= days):
            #print (dateCounter)
            if (dateCounter == 1):
                totalDays += 1
            dateCounter += 7
        
        dateCounter = dateCounter - days

print (totalDays)
        
