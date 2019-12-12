
# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?
'''
list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append(5)

list2.append([5, 6, 7])

# to check, you can print them out using the print statements below.

#print "showing list1 and list2:"
print list1
print list2
'''
import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

random_list = []
list_length = 20

def populating_list():
	while len(random_list) < list_length:
		random_list.append(random.randint(0, 10))
		print random_list
	return random_list








#print len(mylist)

#print mylist.append(random_number())


	



#mylist.append(random_number())

#print 'my lucky number is : ' + str(random_number())

