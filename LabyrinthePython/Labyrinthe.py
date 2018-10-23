# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, elements, sortie):
		self.robot = robot
		self.grille = elements
		self.sortie = sortie


	def aff_laby(self):
		cle = self.grille.keys()
		for elem in cle:
			if elem == self.robot :			#le robot as bougé
				print('X',end='')
				
			elif self.grille[elem] == 'X' and elem != self.robot :
				print(' ',end='')
				self.grille[elem] = ' '
			else:
				print (self.grille.get(elem),end='')