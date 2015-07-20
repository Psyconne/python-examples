ten_things = "Apple Orange Banana Carrot"
print "\nWait there are not 10things. Okai let's fix that"
stuff = ten_things.split(' ')
more_stuff = ["one", "two", "school", "books", "sky", "home"]

while len(stuff) != 10:
	next_stuff = more_stuff.pop()
	print "adding: ", next_stuff	
	stuff.append(next_stuff) 
	print "There are %d items" %len(stuff)

#['Apple', 'Orange', 'Banana', 'Carrot', 'home', 'sky', 'books', 'school', 'two', 'one']
print "That's it: \n", stuff

print "\n Okai, let's do some things with stuff"

print stuff[-1]
print stuff[1]

#one
print stuff.pop() # this is how python do his job ===> pop(stuff) 

#Apple Orange Banana Carrot home sky books school two
print ' '.join(stuff)

#Banana#Carrot#home
print '#'.join(stuff[2:5])
#That extracts a "slice" from the stuff list that is from element 3 to element 4, meaning it does not include element 5.
