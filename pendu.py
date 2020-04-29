# -*- coding: utf-8 -*-

from random import randrange
from fonctions import *
import os

# début de partie le joueur donne son nom
# si aucun score enregistré -> score = 0 pts => {'nom_joueur' : 0}

# ouvre le fichier 'liste_mots.txt' contenant les mots à trouver, lis le fichier et transforme la chaîne de mots en
# liste
scores = dump_scores()
affichage_scores(scores)

nom_joueur = entrer_nom_joueur(scores)

with open('liste_mots.txt', 'r') as fichier_txt:
    liste_mots = fichier_txt.read()
    liste_mots = liste_mots.split("\n")

# appelle la fonction selection_niveau() qui renvoie la longueur max des mots en fonction du niveay choisi par le joueur
# stocke la longueur max dans la variable 'longueur_mot'
longueur_mot = selection_niveau()

# choisis un mot au hasard (random) dans la liste (effectue un random.randrange sur l'index de liste_mots en
# respectant la longueur de la liste)
liste_mots_tries = [mot for mot in liste_mots if len(mot) < longueur_mot]
mot_choisi = liste_mots_tries[randrange(0, len(liste_mots_tries) - 1)]

# Vérifie si une 'lettre' est dans le 'mot' et affiche le mot avec des étoiles sur les lettres qui n'y sont pas
# def verifier_lettre(lettre, mot) 
mot_choisi = list(mot_choisi)
nbre_coups = 8
# Debogage!!!
#print(mot_choisi)
# Debogage!!!

# appel de la fonction deviner_mot() qui fait deviner le mot au joueur
# renvoie le nombre de points en fonction du nombre de coups restants au moment où le mot est trouvé
nbre_points = deviner_mot(mot_choisi, nbre_coups )
scores[nom_joueur] = nbre_points

with open('donnees','wb') as fichier:
    fichier_scores = pickle.Pickler(fichier)
    fichier_scores.dump(scores)

print(scores)

# mot de 8 lettres max choisi au hasard dans une liste
# joueur saisi une lettre par tour (vérifier que c'est bien le cas (len(mot))

# si lettre est dans le mot 
# afficher la (ou les) lettre(s) dans le mot à la bonne place
# mettre etoiles à la place des autres lettres

# 8 coups maximum -> sinon partie perdu
# si mot trouvé -> score += nbre de coups restants

# os.system("pause")
