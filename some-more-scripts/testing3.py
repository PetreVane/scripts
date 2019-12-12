'''
testing = 'cel mai bine e acasa'

print testing.find('bine')
ioana = testing.find('mai')
#print ioana
petre = len('ioanaaaaaaa')
print petre

def acasa():
	if petre == 10:
		print 'merge si asa'
	else:
		print 'asa nu merge'

acasa()
'''
'''from random import randint

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "4"
    else:
        return "5"
#print random_noun()
#print random_noun()


def math():
	if random_noun() == 4:
		return 'equality to 4'
	else:
		return 'equality to 5'
print math() 
'''

'''
def length_noun():
	length = len(random_noun())
	if length < 4:
		return 'are 4 caractere'
	if length < 6:
		return 'are 5 caractere'
	else:
		return 'numar de caractere indisponibil'

print length_noun()
'''

    
test_string_1 = "This is a good NOUN to use when you VERB your food"

print'NOUN' in test_string_1

def string(sentence):
	processed = sentence
	processed = processed.replace('NOUN', 'noun')
	return processed

print string(test_string_1)






