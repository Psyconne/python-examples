try:
	x = float(raw_input('Enter your number > '))
	inverse = 1.0/x
except ValueError:
	print "You should enter an int or float"
except ZeroDivisionError:
	print "Infinity"
finally:
	print "The may or may not have been an exception"
print "The inverse: ", inverse
