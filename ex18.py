def print_two(*arg): #indent the body of every function
	arg1, arg2 = arg
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):#::::::::::::::: 
	print "arg1: %r" % arg1

def print_none():
	print "I got none"

print_two("Imane", "Marouane")
print_two_again("Me", "Him")
print_one("One")
print_none()
