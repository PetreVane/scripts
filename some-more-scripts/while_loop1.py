
# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
#print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the  
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be 
# of length 20
def random_numbers():
	numbers = random.randint(0, 10)
	return numbers

#print random_numbers()

#print len(random_list)
random_list = []
#print len(random_list)

#list_length = 20

def populating_list(mylist):
	list_length = 0
	while list_length <= 20:
		random_list.append(random_numbers())
		return random_list
	list_length += 1



print populating_list(random_list)



# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.


# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
#print random_list
