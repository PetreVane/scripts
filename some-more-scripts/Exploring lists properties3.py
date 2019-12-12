
'''
Generate a random integer between 0 and 10
Add this random integer to our list
Do we have a list of length 20 yet?
If not, we loop back up and go through steps 1 to 3 again while length of the list is less than 20
'''

import random

# We then print a random integer using the random.randint(start, end) function
#print "Random number generated: " + str(random.randint(0,10))

random_list = []
list_length = 20

def populating_list(mylist):
	list_length = 0
	while len(random_list) < 20:
		random_list.append(random.randint(0, 10))
		#return random_list
	list_length += 1

populating_list(random_list)

print random_list


def count(number):
	for elements in random_list:
		return random_list.count(number)

#print count(0)


count_list = [0] * 11

def counting_occurences(): 
	count_list.pop()
	count_list.insert(0, count(0))
	count_list.pop()
	count_list.insert(0, random_list.count(1))
	count_list.pop()
	count_list.insert(0, random_list.count(2))
	count_list.pop()	
	count_list.insert(0, random_list.count(3))
	count_list.pop()
	count_list.insert(0, random_list.count(4))
	count_list.pop()
	count_list.insert(0, random_list.count(5))
	count_list.pop()
	count_list.insert(0, random_list.count(6))
	count_list.pop()
	count_list.insert(0, random_list.count(7))
	count_list.pop()
	count_list.insert(0, random_list.count(8))
	count_list.pop()
	count_list.insert(0, random_list.count(9))
	count_list.pop()
	count_list.insert(0, random_list.count(10))
	return count_list

counting_occurences()
print count_list


