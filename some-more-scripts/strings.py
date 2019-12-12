# Asta este printre primele functii rezolvate fara sa ma uit la solutie
# Joi, 8 decembrie 2016, Odense, Danemarca; 20:00

# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word.

from random import randint

def random_noun():
	random_numb = randint(0, 1)
	if random_numb == 0:
		return "sofa"
	else:
		return "ilana"
random_noun()

def random_verb():
	random_numb = randint(0, 1)
	if random_numb == 0:
		return "run"
	else:
		return "kayak"
random_verb()
 
def word_transformer(word):
	if word == "VERB":
		return random_verb()
	if word == "NOUN":
		return random_noun()
	else:
		return word[0]

def process_madlib(mad_lib):
    #processed = "mad_lib"
    if mad_lib.find('NOUN') == 'NOUN':
    	return random_noun
    if mad_lib.find('VERB') == 'VERB':
    	return random_verb
    else:
    	return "failure"

#test_string_1 = "This is a good NOUN to use when you VERB your food"
print process_madlib('NOUN')
#print word_transformer("mama")
#print word_transformer("NOUN")
#print word_transformer("VERB")
	
