# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import fonctions
import pickle

from fonctions import calc_deplac
from carte import Carte
from Labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
noms = []
laby = Labyrinthe(0,0,1)
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-4].lower()
		if nom_carte[5:].lower() == 'save_':
			print('Voulez vous rejouer la partie précédente ?')
			check = input('[y/n]')
			if check == 'y':
				with open(chemin, 'r') as fichier:
					contenu = fichier.read()
					laby = carte.labyrinthe
				
				remove(chemin)
			else:
				print('Ok, chargement des autres cartes ...')
		else:
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				# Création d'une carte, à compléter
				map = Carte(nom_carte, contenu)
				cartes.append(map)
				noms.append(nom_carte)

# On affiche les cartes existantes
if laby.robot != 0:
	print('Chargement de l\'ancienne partie ...')
	print('\n\n\n')

else:
	print("Labyrinthes existants :")
	for i, carte in enumerate(cartes):
		print("  {} - {}".format(i + 1, carte.nom))

	c = input('Quel labyrinthe voulez vous faire ? (Saisir le chiffre)\n')
	choix = int(c)
	print("\n\n\n\n\n\n\n\n")
	carte = cartes[choix-1]
	laby = carte.labyrinthe
	chemin_carte_ouverte = noms[choix-1]

#sauvegarde nom de la carte pour une sauvegarde si besoin


print("Pour vous déplacer: saisir la première lettre de la direction voulue(n, s, e, o) \nsuivie du nombre de case choisi [1-9] (si une seule case, ne saisir que la lettre)\nPour quitter, saisissez q\n")

#print(laby.sortie)
while laby.robot != laby.sortie:
	laby.aff_laby()
	saisie = input("Où voulez vous aller ?")
	
	laby = calc_deplac( laby, saisie, chemin_carte_ouverte) #retourne un laby avec la position du robot

print('Bravo, relancez le programme si vous voulez de nouveau vous évader')

# Si il y a une partie sauvegardée, on l'affiche, à compléter
# ... Complétez le programme ...



os.system("pause")