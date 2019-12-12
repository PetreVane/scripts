
# Wednesday, December 7, 13:16, Odense, Denmark

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.


def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))


#print biggest(3,5,7)
#print bigger (5,9)


def median(a,b,c):
	higher = biggest(a,b,c)
	if higher==a:
		return bigger (b,c)
	if higher==b:
		return bigger(a,c)
	else:
		return bigger(a,b)


print(median(3,1,2))
print(median(7,8,7))
print(median(9,3,6))
print(median(1,2,3))


# the line of codes bellow, are part of the figuring out process, which
#unfortunately, has failed without solution.
    
'''def smaller(a,b):
    if a<b:
        return a
    else:
        return b
    
def smallest(a,b,c):
    return smaller(a, smaller(a,b))'''


'''def median(a, b, c):
    #higher= biggest(a,b,c)
    #return higher
    #lower=smallest(a,b,c)
    if a<biggest and a>smallest:
        return a
    elif b<higher and b>lower:
        return b
    elif c<higher and c>lower:
        return c
    else:
        print ("failure")'''
        
#print( median(1,2,3))
'''print smallest(3,1,2)
print smaller (3, 5)
print bigger(4, 7)
print biggest(4,7,9)'''

'''def median(a,b,c):
	if a!=smallest and a!=biggest:
		return a
	if b!=smallest and b!=biggest:
		return b
	if c!=smallest and c!=biggest:
		return c
print (median(5, 2, 3))'''





