print "I'm 6'2\" inch" #escape double-quote
print 'I\'m 6"2 inch' #escape single-quote
backslash = "I'm \\ a \\ cat."
tabby_cat = "\tI'm tab in."
formfeed = "Heeeee\fllo"
bell_and_backspace = "\bHi \a and this is \b yes " 
print backslash
print tabby_cat
print formfeed
print bell_and_backspace
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
