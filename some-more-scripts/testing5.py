

from random import randint 

def random_verb():
	random_verb = randint(0, 1)
	if random_verb == 0:
		return "run"
	else:
		return "kayak"
#print random_verb() 

def random_noun():
	random_noun = randint(0, 1)
	if random_noun == 0:
		return "sofa"
	else:
		return "llama"
#print random_noun()

test_string_1 = "This is a good NOUN to use when you VERB your food"

def word_transformer(word):
	if "NOUN" in word:
		processed = word.replace("NOUN", random_noun())
		return processed

print word_transformer(test_string_1)
	
'''
		if word == "NOUN":
			return random_noun()
			if word == "VERB":
				return random_verb()
			else:
				return word[:1]
#print word_transformer('VERB')
print word_transformer(test_string_1)'''

'''
def process_madlib(madlib):
	processed = word_transformer(test_string_1)
	madlib = processed
	if "VERB" in processed:
		return word_transformer()
	else:
		return processed
print process_madlib(test_string_1)
'''

