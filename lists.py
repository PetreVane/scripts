

student_names = ["Mark", "Petre", "Ioana"]

if "Mark" in student_names:
	print ("That is correct")
	
student_names.append ("Daniel")
print ("student_names")
print len(student_names)

name = "teleenciclopedia"
capi = name.replace("e", "i")
print capi

def test():
	if capi:
		print "It exists"
	else:
		print "It does not"
print test()

