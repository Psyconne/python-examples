#Error handling, try except
while True:
	try:
		n = raw_input("Enter an integer: ")
		n = int(n)
		break
	except ValueError:
		print("No valid integer, try again ---!")
print "Great, this is an integer"




