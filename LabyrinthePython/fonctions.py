# -*-coding:Utf-8 -*

""" Fichier de fonctions diverses
	Pour le projet labyrinthe du cours
	sur python
	
"""

from Labyrinthe import Labyrinthe  #fichier puis class
import re

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
	
def calc_deplac (laby, saisie):
	modif = list(saisie)
	
	if len(modif) > 3 or len(modif) < 1 :
		print('Erreur dans votre saisie, nouveau tour. \n')
		return laby
	else: 
		if re.match( r"[nseo]", modif[0]) != None: 	 #Test expression régulières	
			try:							         #vérifie si chiffre ou non
				dep = int(modif[1])
			except:
				dep = 1
			
			pos = list(laby.robot)
			if modif[0] == 'n':
				while dep > 0:
					pos[0] -= 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#pos = ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#pos = sortie
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#pos = mur
						print('Vous ne pouvez pas passer à travers les murs, seul le roi Boo et Casper le peuvent.\n')
						return laby
					
					dep -= 1
				
				return laby
				
			elif modif[0] == 's':
				while dep > 0:
					pos[0] += 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#sortie
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#mur
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
					
				return laby
					
			elif modif[0] == 'e':
				while dep > 0:
					pos[1] += 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#sortie
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#mur
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
					
				return laby
					
			else:
				while dep > 0:
					pos[1] -= 1
					if laby.grille[tuple(pos)] == ' ' or laby.grille[tuple(pos)] == '.':	#ok
						laby.robot = tuple(pos)
					elif laby.grille[tuple(pos)] == 'U':									#sortie
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = tuple(pos)
						return laby
					else:																	#mur
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
					
				return laby
					
