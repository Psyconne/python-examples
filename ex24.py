print "Let's practice everything"
print 'You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs'
poem = '''
	\tThe lovely world
	with logic so firmly planted
	cannot discern \n the needs of love
	nor comprehend passion from intuition
	and requires an explanation
	\n\t\twhere there is none.
'''
print "-------"
print poem
print "-------"

five = 22 - 3 + 10 - 9 / 2
print 'this should be %d' % five

def formula (start):
	jelly = start * 50
	jars = jelly / 1000
	crates = jars / 100
	return jelly, jars, crates

start_point = 1000
beans, jars, crates = formula (start_point)
print 'With a starting point of: %d' %(start_point)
print 'We\'d have %d beans, %d jars and %d crates' %(beans, jars, crates)

start_point = start_point / 10
print 'We can also do it this way, with a new start point of: %d' % start_point
print "We'd have this time, %d beans, %d jars and %d crates" % formula(start_point)
