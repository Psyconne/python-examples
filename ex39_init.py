#you can only use numbers to index into lists
print 'this is a list'
things = ['a', 'b', 'c', 'd']
print 'things: ', things
print things[1]

things[1] = 'r'
print things[1]

print 'things: ', things

#a dict associates one thing to another, no matter what it is
print 'this is dicts'
stuff = {'name': 'El Idrissi', 'age': 22, 'height': 6*10 +8}
print stuff ['name']
print stuff ['age']
print stuff ['height']
stuff ['city'] = 'El jadida'
print stuff['city']
#what order ?
print (stuff)
stuff [3] = 'Nice'
stuff [4] = 'Wow'
#what order ?
print (stuff) 
#to delete
del stuff['city'], stuff[3], stuff[4]
print (stuff)
