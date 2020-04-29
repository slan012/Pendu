# -*- coding: utf-8 -*-

from random import randrange
from fonctions import *
import os

lettre_chiffre = True
niveau_jeu = 1

# début de partie le joueur donne son nom
# si aucun score enregistré -> score = 0 pts => {'nom_joueur' : 0}

# ouvre le fichier 'liste_mots.txt' contenant les mots à trouver, lis le fichier et transforme la chaîne de mots en
# liste
with open('liste_mots.txt', 'r') as fichier_txt:
    liste_mots = fichier_txt.read()
    liste_mots = liste_mots.split("\n")

# choisis un mot au hasard (random) dans la liste (effectue un random.randrange sur l'index de liste_mots en
# respectant la longueur de la liste)
print("Niveau de jeu :\n\n"
      "1 - Facile, les yeux fermés\n"
      "2 - Normal, mais peut mieux faire\n"
      "3 - Difficile, ça commence à causer\n"
      "4 - Hardcore! Accroche toi Huguette!\n")
niveau_jeu = input()
niveau_jeu = int(niveau_jeu)
if niveau_jeu == 1:
    longeur_mot = 4
elif niveau_jeu == 2:
    longeur_mot = 6
elif niveau_jeu == 3:
    longeur_mot = 8
elif niveau_jeu == 4:
    longeur_mot = 9


liste_mots_tries = [mot for mot in liste_mots if len(mot) < longeur_mot]
mot_choisi = liste_mots_tries[randrange(0, len(liste_mots_tries) - 1)]

# Vérifie si une 'lettre' est dans le 'mot' et affiche le mot avec des étoiles sur les lettres qui n'y sont pas
# def verifier_lettre(lettre, mot) 


mot_choisi = list(mot_choisi)
mot_cache = list(mot_choisi)
nbre_coups = 8

for i, element in enumerate(mot_cache):
    mot_cache[i] = '*'
print("[ {} ]".format(" ".join(mot_cache)))

while nbre_coups > 0 and '*' in mot_cache:
    mot_choisi = list(mot_choisi)
    lettre, coup_valide = entrer_lettre()
    for i, element in enumerate(mot_choisi):
        if element == lettre.upper():
            mot_cache[i] = lettre.upper()
    print("\n[ {} ]".format(" ".join(mot_cache)))
    if coup_valide:
        nbre_coups -= 1
        print ("\nNombre de coups restants : {}".format(nbre_coups))

if nbre_coups == 0:
    print("\nPERDU! Nombre de coups max atteint")
    print("\nLe mot était : {}".format(mot_choisi.upper()))
else:
    print("C\'est gagné!! Nombre de coups restants : {}".format(nbre_coups))

# mot de 8 lettres max choisi au hasard dans une liste
# joueur saisi une lettre par tour (vérifier que c'est bien le cas (len(mot))

# si lettre est dans le mot 
# afficher la (ou les) lettre(s) dans le mot à la bonne place
# mettre etoiles à la place des autres lettres

# 8 coups maximum -> sinon partie perdu
# si mot trouvé -> score += nbre de coups restants

os.system("pause")
