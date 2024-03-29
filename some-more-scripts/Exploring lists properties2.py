
# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6, 7]
    #return mylist

#print proc(list1)


def proc2(mylist):
    mylist.append(6)
    mylist.append(7)
    #return mylist


#print proc2(list1)

# Can you explain the results given by the print statements below?


print "demonstrating proc"
print list1
proc(list1)
print list1

print
print "demonstrating proc2"
print list2
proc2(list2)
print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4,5]
list3 += [6, 7]

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 
