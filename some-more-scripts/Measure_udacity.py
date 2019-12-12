$
# Define a procedure, named measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

p = ['Adrian', 'Umika', 'Ana']

#print p.index('Umika')
print len(p)
l =''.join(p[:])
print l
print len(l)
print l.count('U')


#print reduce(p, [0, 3])
#print p.remove('mika')



def measure_udacity(list):
	list = ''.join(list[:])
	return list.count('U')

print measure_udacity(['Dave','Sebastian','Katy'])
print measure_udacity(['Umika','Umberto', 'Umbrella'])


squares = []
for x in range(3):
	squares.append(x**2)
print squares



sentence = ['this','is','a','sentence']
print' '.join(sentence)
print sentence
#print sentence.join("-")
