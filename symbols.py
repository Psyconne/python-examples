#use del to remove from a list
print "\nuse of del\n"
values = [100, 200, 300, 400, 500, 600]
print "values: ",values
del values[2]
print values
#use remove to remove from a list 

print "\nuse of remove\n"
values = [100, 200, 300, 400, 500, 600]
print "values: ",values
values.remove(100)
print values

print "\nremove always removes the first match\n"

list_ofnumbers = [10, 20, 20, 20, 10, 20]
print "list_ofnumbers: ",list_ofnumbers
list_ofnumbers.remove(20)
print list_ofnumbers

print "\nOkai, let's try another thing\n"

elements = ["sara", "imane", "hajar", "raja"]
print "elements: ",elements
del elements[:1]
print elements

elements = ["sara", "imane", "hajar", "raja"]
del elements[1:3]
print elements

elements = ["sara", "imane", "hajar", "raja"]
del elements[2] 
print elements

print "\nnow with dictionaries, delete the pair with a key blue\n"
colors = {"red":10, "blue":20, "black":30}	
print "colors: ",(colors)
del colors["blue"]
print(colors)

print "\nOkai, Let's try assert, with a = b\n"
#when doing return maxi, the assertionError doesn't raise 
def max_two(a, b):
	maxi = 0
	if a < b:
		maxi=b
	elif b < a:
		maxi=a
	assert (maxi == a or maxi == b) and maxi >= a and maxi >= b

print "\nenter a: "
a = int(raw_input('> '))
print "\nenter b: "
b = int(raw_input('> '))
print max_two(a, b)


