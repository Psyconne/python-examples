x = "There are %d types of people" % 10 #this is x
binary = "binary" # this is binary
not_binary = "don't" #this is not
y = "those who know %s and those who %s." % (binary, not_binary) # if there's more than 2, than ()
print x
print y
print " I said: %r." % x # %r print all the line, used for debugging 
print " I also said: '%s'." % y
hilarious = False
joke_eval = "so funny? %r"
print joke_eval % hilarious
w = "This is the left side of a string .."
e = "with a right side"
print w + e # concatenation 

