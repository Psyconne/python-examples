from sys import argv
script, filename = argv
txt = open(filename, 'w') #write mode
print "Hello"
print "Truncate the file " 
txt.truncate() #erase the content of the file
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

txt.write(line1 +'\n'+line2 +'\n'+line3+'\n') #write a string in a file in one line :D 
txt.close() #must close the file to read the new one !!
txt_new = open(filename, 'r')
print "And the file is "
print txt_new.read()
txt_new.close()
