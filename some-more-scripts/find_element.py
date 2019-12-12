
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#list = ['ioana', 'element', 'acasa']

#print list.index('element')
#print list[1]

# this is my solution to this problem.
# Here is the result I have received: 
# Incorrect. Your code did not find the correct index -1 for list ['Job', 'Andy', 'Peter', 'Sean', 'Michael', 'Gundega', 'Sarah'] and element 'Kathleen'. Your submission passed 10 out of 12 test cases.


def find_element(list, element):
		if element not in list:
			return '-1'
		else:
			return list.index(element)

print find_element([],3)
print find_element(['Job','Andy','Peter', 'Sean', 'Michael', 'Gundega', 'Sarah'],'Kathleen')
print find_element(['Job','Andy','Peter', 'Sean', 'Michael', 'Gundega'],'Gundega')
