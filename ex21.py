def add (a, b):
	print "ADDING %d + %d " %(a, b)
	return a + b
def sub (a, b):
	print "SUBSTRACTING %d - %d " %(a, b)
	return a - b
def mult (a, b):
	print "MULTIPLYING %d * %d " %(a, b)
	return a * b
def divide (a, b):
	print "DIVIDING %d / %d " %(a, b)
	return a / b
print "Let's do some maths"
age = add(22, 3)
height = sub (198, 54)
weight = mult (6, 17)
iq = divide (100, 3)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)
#a puzzle
print "Here's a puzzle"
what = add(age, sub(height, mult(weight, divide(iq, 2)))) #inside out 
print "That's becomes: ", what, "Can you do it by hand?"
