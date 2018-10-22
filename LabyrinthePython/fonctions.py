# -*-coding:Utf-8 -*

""" Fichier de fonctions diverses
	Pour le projet labyrinthe du cours
	sur python
	
"""

from Labyrinthe import Labyrinthe  #fichier puis class

def creer_labyrinthe_depuis_chaine(chaine):
	elements = {}
	lignes = chaine.split("\n")
	for ligne in lignes:
		for colonne in ligne:
			if colonne == "X":
				robot = (lignes.index(ligne), lignes.index(colonne))
			else:
				elements[(lignes.index(ligne), lignes.index(colonne))]= str(colonne)

	labyrinthe = Labyrinthe(robot, elements)
	
	return labyrinthe