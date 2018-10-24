# -*-coding:Utf-8 -*

""" Fichier de fonctions diverses
	Pour le projet labyrinthe du cours
	sur python
	
"""

from Labyrinthe import Labyrinthe  #fichier puis class
import re
import pickle
import sys

def creer_labyrinthe_depuis_chaine(chaine):
	elements = {}
	robot = 0
	lignes = chaine.split("\n")
	for ligne in enumerate(lignes):
		for char in enumerate(ligne[1]):
			if char[1] == "X":
				robot = (ligne[0],char[0])
				elements[(ligne[0],char[0])] = char[1]
			elif char[1] == 'U':
				sortie = (ligne[0],char[0])
				elements[(ligne[0],char[0])] = char[1]
			else:
				elements[(ligne[0],char[0])] = char[1]
		
		elements[ (ligne[0], (char[0]+1) ) ] = "\n"
		
	return Labyrinthe(robot, elements, sortie)
	
def calc_deplac (laby, saisie, chemin_carte_ouverte):
	"""
		Calcul la position du robot en fonction du déplacement saisie par l'utilisateur,

		Ou lance la sauvegarde si elle est demandé par le joueur
	"""
	modif = list(saisie)
	
	if len(modif) > 3 or len(modif) < 1 :
		print('Erreur dans votre saisie, nouveau tour. \n')
		return laby
	else: 
		if re.match( r"[nseoNSEO]", modif[0]) != None: 	 #Test expression régulières	
			try:							         	 #vérifie si chiffre ou non
				dep = int(modif[1])
			except:
				dep = 1
			
			pos = list(laby.robot)
			if modif[0].lower() == 'n':
				while dep > 0:
					pos[0] -= 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#pos = ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#pos = sortie
						print('\n\n\nBravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#pos = mur
						print('\nVous ne pouvez pas passer à travers les murs, seul le roi Boo et Casper le peuvent.\n')
						return laby
					
					dep -= 1
				
				return laby
				
			elif modif[0].lower() == 's':
				while dep > 0:
					pos[0] += 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#pos = sortie
						print('\n\n\nBravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#pos = mur
						print('\nVous ne pouvez pas passer à travers les murs, seul le roi Boo et Casper le peuvent.\n')
						return laby
					
					dep -= 1
					
				return laby
					
			elif modif[0].lower() == 'e':
				while dep > 0:
					pos[1] += 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#pos = sortie
						print('\n\n\nBravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#pos = mur
						print('\nVous ne pouvez pas passer à travers les murs, seul le roi Boo et Casper le peuvent.\n')
						return laby
					
					dep -= 1
					
				return laby
					
			else:
				while dep > 0:
					pos[1] -= 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#pos = sortie
						print('\n\n\nBravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#pos = mur
						print('\nVous ne pouvez pas passer à travers les murs, seul le roi Boo et Casper le peuvent.\n')
						return laby
					
					dep -= 1
					
				return laby
		
		elif re.match( r"[Qq]", modif[0]) != None:
			######Lancer la sauvegarde			
			sauvegarde_partie(laby ,chemin_carte_ouverte)
			print('Vous avez demander la fermeture du programme')
			sys.exit(0)
		else:
			print('Erreur dans la saisie\n')
			return laby
			
def sauvegarde_partie (objet, chemin_carte_ouverte):
	""" Fonction de sauvegarde de la partie,
		Enregistre dans un fichier, avec le préfixe save_
		Efface l'ancienne partie si il y a deja un fichier existant
	"""
	
	with open('cartes/save_'+chemin_carte_ouverte+'.txt', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(objet)
		
	print('Fin de la sauvegarde')
		
		
		