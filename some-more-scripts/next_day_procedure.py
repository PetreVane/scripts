
###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

#print nextDay(1999, 12, 31)


'''
pseudocode:

days = 0

while date1 is before date2:
	date1 = day after date1
	days +=1
retunr days 
'''

def nextDay(year, month, day):
	if day < 30:
		return year, month, day +1
	else:
		if month < 12:
			return year, month +1, 1
		else:
			return year +1, 1, 1


def dateIsbefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			return day1 < day2
				
	return False 

#print dateIsbefore(2016,03,8,2015,11,21)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	days = 0
	while dateIsbefore(year1, month1, day1, year2, month2,day2):
		year1, month1, day1 = nextDay(year1, month1, day1)
		days +=1
	return days
#print daysBetweenDates (2016, 11, 21, 2015, 12, 27)

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)            
test()



