from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, i'm the %s script " % (user_name, script)
print "So where do you live %s ? " % user_name
live = raw_input(prompt)
print "What is your computer %s ? " % user_name
computer = raw_input(prompt)
print """
So you are %r, and you live in %r, and you have a %r computer. Nice
""" % (user_name, live, computer) 
