
from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
#print random_verb()
        
def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"
#print random_noun()

def word_transformer(word):

    if "NOUN" in word:
        return random_noun()
    if "VERB" in word:
        return random_verb()
    else:
        return word[0]
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
# This is the solution that has been propossed by Sean ( the guy who teaches intro to programming nanodegree). It's far more complicated than expected and it doesn't seem to work
def process_madlib(madlib):
	processed = " "
	index = 0
	box_frame = 4
	while index < len(madlib):
		frame = madlib[index:index + box_frame]
		to_add = word_transformer("NOUN")
		processed += to_add
		if len(to_add) == 1:
			index += 1
		else:
			index += 4
		return processed

print process_madlib(test_string_1)
#print process_madlib(test_string_2)