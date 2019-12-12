# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
	country = thing[0]
	capital = thing[1]
print country + ' it s a messed up test' + capital 

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country


def sum_list(list):
	for numbers in list:
		adding = list[0] + list[1]+ list[2]
	return adding

print sum_list([1, 4, 2])


def another_sum(list):
	result = 0
	for e in list:
		result = result + e
	return result
print another_sum([2, 5, 6, 6])


