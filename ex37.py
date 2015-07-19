def f(x):
	return x**2
print f(4)

def incrementor (n): 
	return lambda x: x+n

g = incrementor (3)
print g(34)
print incrementor(2)(10)

foo = [1, 22, 9, 12, 32]
print filter (lambda x: x%3 == 0, foo)
print map(lambda x: x*2+10, foo)
