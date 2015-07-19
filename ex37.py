#
def f(x):
	return x**2
print f(4)
#incrementor
def incrementor (n): 
	return lambda x: x+n

g = incrementor (3)
print g(34)
print incrementor(2)(10)

foo = [1, 22, 9, 12, 32]
#filter
print filter (lambda x: x%3 == 0, foo)
#map
print map(lambda x: x*2+10, foo)
#sum
print reduce(lambda x, y: x+y, foo)
#prime numbers
nums = [1, 13, 22, 24, 52, 12, 7, 8, 11]
for i in range (2, 7):
	nums = filter (lambda x: x==i or x%i, nums)
print nums
