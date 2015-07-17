# A while-loop will keep executing the code block under it as long as a boolean expression is True.
i = 0
numbers = []
while i < 6:
	print 'i at the top is %d' %i #i=0
	numbers.append(i) #i=O
	i+=1 #i=1
	print 'numbers now ', numbers #[0]
	print 'i at the bottom is %d' %i #i=1
print 'The numbers: '
for n in numbers:
	print n # 0 1 2 3 4 5

