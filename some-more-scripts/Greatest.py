
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.
def greatest(list_of_numbers):
    if len(list_of_numbers) > 0:
    	higher = max(list_of_numbers)
    	return higher
    else:
    	return 0 

'''
def greatest(list_of_numbers):
	big = 0
	for i in list_of_numbers:
		if i > big:
			big = i
			return big
		else:
			return 0 
'''
print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0
print greatest([1000, 3, -1])
