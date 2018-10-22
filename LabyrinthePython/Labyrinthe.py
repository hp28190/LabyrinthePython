# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, elements):
		self.robot = robot
		self.grille = elements

	def __repr__(self):
		elementa = 0
		cles = self.grille.keys()	#récupération des tuples de clé
		print (cles)
		for element in sorted(cles):	#tri des tuples dans l'ordre croissant
			tuple =  cle[element]
			elementb = b[0] 
			
			if elementb != elementa :
				print('\n')
			aff = self.grille.get(cle[element])
			elementa = tuple[0] 