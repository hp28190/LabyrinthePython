# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import fonctions

from fonctions import calc_deplac
from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			# Création d'une carte, à compléter
			map = Carte(nom_carte, contenu)
			cartes.append(map)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

c = input('Quel labyrinthe voulez vous faire ? (Saisir le chiffre)\n')
choix = int(c)
print("\n\n\n\n\n\n\n\n")

print("Pour vous déplacer: saisir la première lettre de la direction voulue(n, s, e, o) suivie du nombre de case choisi [1-9] (si une seule case, ne saisir que la lettre)\n")
	
carte = cartes[choix-1]
laby = carte.labyrinthe
#print(laby.sortie)
while laby.robot != laby.sortie:
	laby.aff_laby()
	saisie = input("Où voulez vous aller ?")
	
	laby = calc_deplac( laby, saisie) #retourne un laby avec la position du robot

print('Bravo, relancez le programme si vous voulez de nouveau vous évader')

# Si il y a une partie sauvegardée, on l'affiche, à compléter
# ... Complétez le programme ...



os.system("pause")