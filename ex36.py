#-*- coding:utf-8 -*-
from sys import argv
import random

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
	print 'Vous voulez un vendeur, de legumes, de vetements ou d\'electromenagers ?'
	choix = raw_input('> ')
	if choix == 'legumes':
		print 'legumes'
	elif choix == 'vetements':
		print 'vetements'
	elif choix == 'electomenagers':
		print 'electromenagers'
	else:
		prompt('legumes, vetements, ou electromenagers')
		vendeur_room()


#dentiste_room
def dentiste_room():
	print 'C\'est le cabinet du dentiste, voulez vous prendre un rendez vous, ou prendre la queue? '
	choix = raw_input('> ')
	if 'rendez' in choix:
		print 'Quel jour choisirez vous? '
		jour = raw_input('> ')
		print 'A quelle heure voulez vous un rendez vous?'
		heure = int(raw_input('> '))
		prompt('Rendez vous le')
		print jour, heure
	elif 'queue' in choix:
		rand_number = random.randint(1,100)
		print 'Votre numero est %d' %rand_number
		print 'Voulez vous une magazine?\n Yes or No ?'
		magazine = raw_input('> ')
		if magazine == 'yes':
			j = 0			
			list_magazine = ['Telquel', 'Femme du maroc', 'Nichane']
			for i in list_magazine:
				print 'Magazine %d: %s' %(j, i)
				j+=1
		else:
			prompt('Bonne chance')
	else:
		prompt('Rendez vous ou queue !!')
		dentiste_room()

#prompt()
def prompt(smt):
	print smt, '\n'

#start()
def start():
	prompt('Tu choisis: \n Coiffeur, vendeur, dentiste ?')
	choix = raw_input('> ')
	
	if choix == 'coiffeur':
		coiffeur_room()
	elif choix == 'vendeur':
		vendeur_room()
	elif choix == 'dentiste':
		dentiste_room()
	else:
		prompt('Choix erroné')
		start()	

print nom
start()




