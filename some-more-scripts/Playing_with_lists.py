
# Every entry in the following list is itself a list

nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]

#print "What do you think this will print?"
#print first_concept 

#print "Since first_concept was itself a list, we can access its elements"
first_title = first_concept[0]
#print first_title
first_description = first_concept[1]
#print first_description


#print "What will this print?"
#print first_title
#print first_description


#Nested lists


Beatles = [['John', 1940], ['Paul', 1942],
['George', 1943], ['Ringo', 1940]]

print Beatles[3][0]