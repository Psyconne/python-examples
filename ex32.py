the_count = [1,2,3,4,5]
fruits = ['banana','apple','pears','oranges'] #this is a list
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count: #this is a for-loop
	print 'this is a count %d' %number
for fruit in fruits:
	print 'this is a fruit %s' %fruit
for i in change:
	print 'i got %r' %i
 
elements = []  #empty list
for i in range(0, 6): #range from 0 to 5
	print 'Adding %d to the list' %i
	elements.append(i) #append is a function that lists understand
for i in elements:
	print 'that was %d' %i
element = [[1,2,3], ['imane', 'marouane'], ['Do you love me ?'], [1, 'yes', 2, 'no']]
for i in element:
	print 'Here we go \n %r' %i
