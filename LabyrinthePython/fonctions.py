# -*-coding:Utf-8 -*

""" Fichier de fonctions diverses
	Pour le projet labyrinthe du cours
	sur python
	
"""

from Labyrinthe import Labyrinthe  #fichier puis class

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
	
	