from sys import argv
script, filename = argv  #parametre from the comand line
file = open(filename) #open a file
print "Here's your %s file " %filename
print file.read() #read from the file and print it to us
file.close()
print "Enter the name of your file"
name_again = raw_input('> ')
file_again = open(name_again) #open a file giving as input
print file_again.read() #read from it
file_again.close()
