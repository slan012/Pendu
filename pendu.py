# -*- coding: utf-8 -*-

from random import randrange
from fonctions import *
import os

print("\n******************** Jeu du Pendu ********************")
# Fonction dump_scores() lit le
scores = dump_scores()
if scores != {}:
    affichage_scores(scores)

# On demande au joueur s'il souhaite conserver son score à la fin de la partie
# Si oui, il devra renseigner son nom dans la fonction entrer_nom_joueur()
enregistrer_partie = str()
while enregistrer_partie.lower() != 'o' and enregistrer_partie.lower() != 'n':
    enregistrer_partie = input("\nVeux-tu enregistrer ton score à la fin de la partie (o/n) ? ")
    if enregistrer_partie.lower() == 'o':
        nom_joueur = entrer_nom_joueur(scores)
        enregistrement_partie = True
    else:
        enregistrement_partie = False

# On va lire la liste des mots dans le fichier liste_mots.txt
# On l'enregistre dans liste_mots sous forme de liste
with open('liste_mots.txt', 'r') as fichier_txt:
    liste_mots = fichier_txt.read()
    liste_mots = liste_mots.split("\n")

# appelle la fonction selection_niveau() qui renvoie la longueur max des mots en fonction du niveay choisi par le joueur
# stocke la longueur max dans la variable 'longueur_mot'
longueur_mot = selection_niveau()
# choisis un mot au hasard (random) dans la liste (effectue un random.randrange sur l'index de liste_mots en
# respectant la longueur de la liste)
liste_mots_tries = [mot for mot in liste_mots if len(mot) < longueur_mot]

# La partie dur n 'tours' et le joueur a droit a n 'nbre_coups'. Son score en début de partie est 0.
# On choisi un mot au hasard dans la liste et on le stocke dans 'mot_choisi'. On le transforme en liste de caractères
# On appelle la fonction deviner_mot() avec les paramètres et elle nous renvoie le score total à la fin du tour
# On incrémente le score_total
tours = 1
nbre_coups = 11
score_total = 0
while tours <= 4:
    print("\nTour {}".format(tours))
    mot_choisi = liste_mots_tries[randrange(0, len(liste_mots_tries) - 1)]
    mot_choisi = list(mot_choisi)
    score_partie = deviner_mot(mot_choisi, nbre_coups )
    score_total += score_partie
    tours +=1

print("Ton score final : {}".format(score_total))
# Si le joueur a choisi d'enregistrer son score, on l'enregistre dans le dcitionnnaire 'scores' que l'on envoie dans
# le fichier 'donnees'
if enregistrement_partie :
    scores[nom_joueur] = score_total
    with open('donnees','wb') as fichier:
        fichier_scores = pickle.Pickler(fichier)
        fichier_scores.dump(scores)

print("\nMerci et à bientôt!\n")

os.system("pause")
