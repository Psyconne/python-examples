from sys import argv
from os.path import exists
script, from_file, to_file = argv
infile = open (from_file)
indata = infile.read()
out_file = open (to_file, 'w')
out_file.write(indata)
print 'Done Done Done'
infile.close()
out_file.close()
file_new = open (to_file)
print file_new.read()
file_new.close()
