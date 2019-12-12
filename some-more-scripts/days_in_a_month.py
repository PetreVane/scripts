
# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#print days_in_month.index(31)
#print days_in_month[6]



# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.
#month_number1 = days_in_month.index(30)
#print month_number1
#print days_in_month[month]

def how_many_days(month):
	month_number = days_in_month[month -1]
	return month_number
	

print how_many_days(4)


#print how_many_days(4)
#>>> 31

#print how_many_days(9)
#>>> 30