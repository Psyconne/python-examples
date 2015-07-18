from sys import exit #abort the program
def gold_room():
	print 'this room is full of gold, how much do you take?'
	choice = raw_input('> ')
	if '0' in choice  or '1' in choice: #a number with 1 or 0
		how_much = int(choice)
	else:
		dead('Man, Learn to type a number')
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead('you greedy !! ')

def bear_room():
	print "There is a bear here"
	print "The bear has a bunch of honey, he's in front of another door"
	print "How are you going to move the bear?"
	bear_moved = False
	while True:
		choice = raw_input('> ')
		if choice == "take honey":
			dead('The bear .. slap you ')
		elif choice == "taunt bear" and not bear_moved:
			print 'the bear has moved from the door'
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead('the bear gets pissed off')
		elif choice == "open door" and bear_moved:
			gold_room()	
		else:
			print 'I got no idea what that means'
def something ():
	print 'hhhh'
	choice = raw_input('> ')
	if 'flee' in choice:
		start()
	elif 'head' in choice:
		dead('well that was tasty!')
	else:
		something()
def dead(somt):
	print somt, 'Good job'
	exit(0)
def start():
	print 'You are in a dark room'
	print 'which door do you take'
	choice = raw_input('> ')
	if choice == 'left':
		bear_room()
	elif choice == 'right':
		something()
	else:
		dead('You starve :D :D')
start()
































