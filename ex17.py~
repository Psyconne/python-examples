from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying form %s to %s" % (from_file, to_file)
in_file = open(from_file) #open input file in read mode
indata = in_file.read() #there's a difference between .read and 'r' mode !
print "the input file is %d bytes long" % len(indata) #length
print "Does the output file exists? %r" % exists(to_file) #see the output file if it exists 
print "hit return to continue, Ctrl-c to abort" 
raw_input()
out_file = open(to_file, 'w') #open output file in write mode
out_file.write(indata) #write the input data in the output file
print "All done ---!"
in_file.close() #close both
out_file.close()
