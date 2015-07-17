print "You enter a dark room with two doors. Do you go through door #1 or #2 ?"
door = raw_input('> ')
if door == "1":
	print "There a giant bear here eating a cheese cake, what do you want ?"
	print "1. Scream at the bear"
	print "2. take the cake"
	bear = raw_input('> ')
	if bear == "1":
		print "The bear eats your legs, well done !!! "
	elif bear == "2":
		print "The bear eats your face, good job !!!"
	else:
		print "wrong choice, 1 or 2 ---"
elif door == "2":
	print "You are at el jadida"
	print "1.Eating "
	print "2.take a picture"
	print "3.relax under a tree"
	choice = raw_input('> ')
	if choice == "1":
		print "Bon Appetit !!!"
	elif choice == "2":
		print "Cheeeese, you look awesome"
	elif choice == "3":
		print "Rest darling"
	else:
		print "Enter 1, 2 or 3"
else:
	print "Enter 1 or 2 ---"
