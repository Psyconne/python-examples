#A dictionary is used to map or associate things you want to store to keys you need to get them
#mapping state to abreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#set of state and cities
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print '-' * 10
print 'NY state has: ', cities['NY']
print 'OR state has: ', cities['OR']

#print some states
print '-' * 10
print 'Michigan\'s abreviation is: ', states['Michigan']
print "Florida's abreviation is: ", states['Florida']

#print cities using states
print '-' * 10
print 'Michigan state has: ', cities[states['Michigan']]
print 'Oregan state has: ', cities[states['Oregon']]

#print every state abreviation
print '-' * 10
for state, abrev in states.items():
	print 'state: %s, abrev: %s ' %(state, abrev) 

#print cities
print '-' * 10
for abrev, city in cities.items():
	print 'abrev: %s, city: %s ' %(abrev, city)

#now we do both
print '-' * 10
for state, abrev in states.items():
	print '%s state is abbreviated %s and has city %s ' %(state, abrev, cities[abrev])

#safely get a state that might not be there
print '-' * 10
state = states.get('Texas')

if not state:
	print "Sorry, no Texas"

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print 'The city for the state TX is: %s' %city























