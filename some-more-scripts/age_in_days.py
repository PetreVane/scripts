# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet. 
# Just brainstorm ways you might approach it!


year = 16
leap = year % 100
#print leap



#def isLeapYear(year):

	
#print isLeapYear(2016)
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

#def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    #return days




### Define a simple nextDay procedure, that assumes
### every month has 30 days.

### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)



def nextDay(year, month, day):
	if day < 30:
		return year, month, day + 1
	else:
		if month == 12:
			return year +1, 1, 1
		else: 
			return year,month + 1, 1

#print nextDay(1999, 12, 32)



   

    