from sys import argv
script, input_file = argv
def print_all(f):
	print f.read() #Don't ever forget print with f.read() !!!
def rewind(f):
	f.seek(0) 
def print_line (line_count, f):
	print line_count, f.readline() # print smth , smt else :D
this_file = open(input_file)
print "Let's print the hole file"
print_all(this_file)
print "Now let's rewind" #start over
rewind(this_file)
print "And line by line"
current_line = 1
print_line (current_line, this_file)
current_line = current_line + 1
print_line (current_line, this_file)
current_line = current_line + 1
print_line (current_line, this_file)
	
