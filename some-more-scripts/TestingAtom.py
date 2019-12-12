




from random import randint


def random_number():
	number = randint(0, 10)
	return number
print random_number()

mylist = []
print len(mylist)




def adding_elements():
	return len(mylist)
	while len(mylist) < 20:
		mylist.append(random_number())
	return len(mylist)

print adding_elements()
