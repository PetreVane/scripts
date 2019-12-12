# Few interesting remarks regarding lists, and postion so elements inside the list

#print p[0]
#prints the element on positon 0
#print p.index('i')
# prints the first postion of one particular element. If the same element is present multiple times in the same list, this 'index' comand will only print the first posion of the element, and not the others

p = ['i', '1', 'b', 'c', ['P', 'E', 'T']]


def print_all_elements(p):
	i = 0
	while i < len(p):
		print p[i]
		i = i + 1
	return i

print print_all_elements(p)



def print_elements(p):
	for e in p:
		print e
print_elements(p)







