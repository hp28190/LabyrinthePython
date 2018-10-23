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
	else 
		if re.match( r"[nseo]", modif[0]) != None: 	 #Test expression régulières	
			try:							         #vérifie si chiffre ou non
				dep = int(modif[1])
			except:
				dep = 1
			
			pos = laby.robot
			if modif[0] == 'n':
				while dep > 0:
					pos[0] += 1
					if laby[pos] == ' ' or laby[pos] == '.':
						laby.robot = pos
						return laby
					elif laby[pos] == 'U':	
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = pos
						return laby
					else:
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
					
			elif modif[0] == 's':
				while dep > 0:
					pos[0] -= 1
					if laby[pos] == ' ' or laby[pos] == '.':
						laby.robot = pos
						return laby
					elif laby[pos] == 'U':	
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = pos
						return laby
					else:
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
			elif modif[0] == 'e':
				while dep > 0:
					pos[1] += 1
					if laby[pos] == ' ' or laby[pos] == '.':
						laby.robot = pos
						return laby
					elif laby[pos] == 'U':	
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = pos
						return laby
					else:
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1
			else:
				while dep > 0:
					pos[1] -= 1
					if laby[pos] == ' ' or laby[pos] == '.':
						laby.robot = pos
						return laby
					elif laby[pos] == 'U':	
						print('Bravo vous êtes sorti du labyrinthe\n')
						laby.robot = pos
						return laby
					else:
						print('Vous ne pouvez pas passer à travers les murs, seul Boo le peux.\n')
						return laby
					dep -= 1