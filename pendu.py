# -*- coding: utf-8 -*-

from random import randrange
from fonctions import *
import os

print("\n******************** Jeu du Pendu ********************")
# Fonction dump_scores() lit le
scores = dump_scores()
if scores != {}:
    affichage_scores(scores)

enregistrer_partie = str()
while enregistrer_partie.lower() != 'o' and enregistrer_partie.lower() != 'n':
    enregistrer_partie = input("\nVeux-tu enregistrer ton score à la fin de la partie (o/n) ? ")
    if enregistrer_partie.lower() == 'o':
        nom_joueur = entrer_nom_joueur(scores)
        enregistrement_partie = True
    else:
        enregistrement_partie = False

    with open('liste_mots.txt', 'r') as fichier_txt:
        liste_mots = fichier_txt.read()
        liste_mots = liste_mots.split("\n")

# appelle la fonction selection_niveau() qui renvoie la longueur max des mots en fonction du niveay choisi par le joueur
# stocke la longueur max dans la variable 'longueur_mot'
longueur_mot = selection_niveau()

# choisis un mot au hasard (random) dans la liste (effectue un random.randrange sur l'index de liste_mots en
# respectant la longueur de la liste)
liste_mots_tries = [mot for mot in liste_mots if len(mot) < longueur_mot]

# appel de la fonction deviner_mot() qui fait deviner le mot au joueur
# renvoie le nombre de points en fonction du nombre de coups restants au moment où le mot est trouvé
tours = 1
nbre_coups = 8
score_total = 0
while tours <= 4:
    print("\nTour {}".format(tours))
    mot_choisi = liste_mots_tries[randrange(0, len(liste_mots_tries) - 1)]
    mot_choisi = list(mot_choisi)
    score_partie = deviner_mot(mot_choisi, nbre_coups )
    score_total += score_partie
    tours +=1

print("Ton score final : {}".format(score_total))

if enregistrement_partie :
    scores[nom_joueur] = score_total
    with open('donnees','wb') as fichier:
        fichier_scores = pickle.Pickler(fichier)
        fichier_scores.dump(scores)

os.system("pause")
