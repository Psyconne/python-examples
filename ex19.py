def cheese_crackers(cheese_count, boxes_crackers):
	print """
	We have %d cheeses!
	And %d boxes of crackers!
	""" %(cheese_count, boxes_crackers)
	print "Alright then"
print "We can give the function numbers directly"
cheese_crackers(20, 30)
print "Or use variables"
cheese_count = 34
boxes_crackers = 12
cheese_crackers(cheese_count, boxes_crackers)
print "We can do maths inside"
cheese_crackers(12+3, 33+45)
print "Or both :D"
cheese_crackers(cheese_count+4, boxes_crackers+10)
