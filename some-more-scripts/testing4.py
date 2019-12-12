
# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

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
    frame = 
    if "NOUN" in word:
        return random_noun()
    if "VERB" in word:
        return random_verb()
    else:
        return word[0]

#print word_transformer("VERB")

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
       
def process_madlib(mad_lib):
    processed = mad_lib
    if "VERB" and "NOUN" in processed:
    	return processed.replace("NOUN", word_transformer("NOUN")).replace("VERB", word_transformer("VERB"))
    else:
    	return "something went wrong"
   
print process_madlib(test_string_1)
print process_madlib(test_string_2)


