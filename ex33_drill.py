def numbers_using_while(limit, pas):
	i = 0
	numbers = []
	while i < limit:
		print 'i at the top of the while %d ' %i
		numbers.append(i)
		i+=pas
	print numbers

numbers_using_while(22, 2)

def numbers_using_for(limit, pas):
	numbers = []	
	for i in range (0, limit, pas):
		print 'this is i %d' %i
		numbers.append(i)
	print numbers

numbers_using_for(20, 3)

