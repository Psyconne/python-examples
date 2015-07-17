from sys import argv
script, nom = argv
#coiffeur_room
def coiffeur_room():
	#couper, makeup, maniscure as choices 
	print 'Vous etes chez le coiffeur, pourquoi vous etes ici ? '
	choix = raw_input('> ')

	if 'coup' in choix:
		#something
		print 'coup'
	elif 'make' in choix or 'up' in choix:
		#something
		print 'make'
	elif choix == 'manicure':
		#something
		print 'manicure'
	else:
		prompt('Mais tu es chez le coiffeur')
		coiffeur_room()

#vendeur_room
def vendeur_room():
	print 'Vous voulez un vendeur, de legumes, de vetements ou d\'electromenagers ?
	choix = raw_input('> ')
	

#dentiste_room
#prompt()
def prompt(smt):
	print 'Hello', nom, '\n', smt
#start()
def start():
	prompt('Coiffeur, vendeur, dentiste ?')
	choix = raw_input('> ')
	
if choix == 'coiffeur':
		coiffeur_room()
	#elif choix == 'vendeur'
	#	vendeur_room()
	#elif choix == 'dentiste'
	#	dentiste_room()
	else:
		prompt('Aucun choix')
		start()	
start()




