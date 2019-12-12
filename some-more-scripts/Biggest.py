
def biggest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    if b>c:
        return b
    else:
        return c

print biggest(3, 6, 9)
print biggest(6, 9, 3)
print biggest(9, 3, 6)
print biggest(3, 3, 9)
print biggest(9, 3, 9)

print max (2,5,7)

i =0
while i<5:
    print i
    i=i+1

x=0
while x!=10:
    x=x+1
    print x



def print_numbers(n):
    i=1
    while i<=n:
        print i
        i=i+1
print_numbers(3)

def test(i):
    i=0
    if i<=30:
        print i
    i=i+1
#print test(2

print "petre vane"




def weekend(day):
    if day=='Saturday' or day=='Sunday':
        return True
    else:
        return False
print weekend('Monday')
print weekend('Saturday')
print weekend('Sunday')    
