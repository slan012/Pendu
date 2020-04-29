# -*- coding: utf-8 -*-

from random import randrange

# début de partie le joueur donne son nom
# si aucun score enregistré -> score = 0 pts => {'nom_joueur' : 0}

# ouvre le fichier 'liste_mots.txt' contenant les mots à trouver, lis le fichier et transforme la chaîne de mots en
# liste
with open('liste_mots.txt', 'r') as fichier_txt:
    liste_mots = fichier_txt.read()
    liste_mots = liste_mots.split("\n")

# choisis un mot au hasard (random) dans la liste (effectue un random.randrange sur l'index de liste_mots en
# respectant la longueur de la liste)
mot_choisi = liste_mots[randrange(0, len(liste_mots) - 1)]

# Vérifie si une 'lettre' est dans le 'mot' et affiche le mot avec des étoiles sur les lettres qui n'y sont pas
# def verifier_lettre(lettre, mot) 

print(mot_choisi)
mot_choisi = list(mot_choisi)
mot_cache = list(mot_choisi)
nbre_coups = 8

for i, element in enumerate(mot_cache):
    mot_cache[i] = '*'

while nbre_coups > 0:
    mot_choisi = list(mot_choisi)
    lettre = input("Lettre : ")
    for i, element in enumerate(mot_choisi):
        if element == lettre.upper():
            mot_cache[i] = lettre.upper()
    print(" ".join(mot_cache))
    nbre_coups -= 1

if nbre_coups == 0:
    print("Nombre de coups max atteint")

# mot de 8 lettres max choisi au hasard dans une liste
# joueur saisi une lettre par tour (vérifier que c'est bien le cas (len(mot))

# si lettre est dans le mot 
# afficher la (ou les) lettre(s) dans le mot à la bonne place
# mettre etoiles à la place des autres lettres

# 8 coups maximum -> sinon partie perdu
# si mot trouvé -> score += nbre de coups restants
