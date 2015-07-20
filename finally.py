#try finally (or clean up clause)
try:
	x = float (raw_input("Enter your number: "))
	inverse = 1.0/x
finally:
	print "\nThere may or may not have been an exception\n"

print "The inverse: ", inverse

