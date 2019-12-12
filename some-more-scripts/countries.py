# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print countries[1][1]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

multiple = countries[0][2] / countries[2][2]
print multiple

name = ['P', 'E','T','R', 'E']
print name
name[2] = 'r'
print name


s = 'Name'
print s[0]
s[0] = 'V'
print s
name = ['P','E','T','R','E']
print name 
# now I am assigning the list to another variable
another_name = name
print another_name
# now I'm changing  elemnts of the list
another_name[0] = 'V' 
print another_name
# the changes are reflected withn both variables
print name 

spy = [0, 0, 7]
#spy[2] = spy[2] + 1
print spy
#print spy.index(7)

def replace_spy(list):
	list[2] = list[2] + 1
	return list

print replace_spy(spy)


spy.insert(2, 8)
print spy

#spy.remove(7)
#print spy

spy.pop(2)
print spy

print len(spy)

p = [0, [0, [0, 1]]]

print len(p) 







