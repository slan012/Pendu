# -*- coding: utf-8 -*-
# fichier rassemblant toutes les fonctions nécessaires à pendu.py
import pickle
# fonction qui vérifie si la lettre tapée par le joueur n'est ni un entier ni un flottant
def entrer_lettre():
    lettre_chiffre = True
    lettre = 'None'
    while lettre_chiffre or len(lettre) != 1:
        try:
            lettre = input("\nLettre : ")
            lettre = int(lettre)
            print('Pas de chiffre!')

        except ValueError:
            try:
                lettre = float(lettre)
                lettre_chiffre = True
                print('Pas de chiffre!')
            except ValueError:
                try:
                    assert len(lettre) == 1
                    lettre_chiffre = False
                    coup_valide = True
                except AssertionError:
                    print("Il ne faut rentrer qu'UNE seule lettre...petit malin!")
    return lettre, coup_valide

# fonction qui demande au joueur de sélectionner un niveau de jeu et adapdte la longueur maximum des mots à trouver
def selection_niveau():
    niveau_jeu = 0
    print("\nChoisis un niveau de jeu :\n\n"
          "1 - Facile, les yeux fermés\n"
          "2 - Normal, mais peut mieux faire\n"
          "3 - Difficile, ça commence à causer\n"
          "4 - Hardcore! Accroche toi Huguette!\n")
    while type(niveau_jeu) != int or niveau_jeu < 1 or niveau_jeu > 4:
        try:
            niveau_jeu = input("Niveau : ")
            niveau_jeu = int(niveau_jeu)
            if niveau_jeu == 1:
                longueur_mot = 4
                print("Niveau sélectionné : Facile")
            elif niveau_jeu == 2:
                longueur_mot = 6
                print("Niveau sélectionné : Normal")
            elif niveau_jeu == 3:
                longueur_mot = 8
                print("Niveau sélectionné : Difficile")
            else:
                longueur_mot = 9
                print("Niveau sélectionné : Hardcore!")
        except ValueError:
            print("Choisis le niveau parmi la liste")


    return longueur_mot

# fonction qui permet le déroulement du jeu. En paramètres : le 'mot_choisi' aléatoirement et le 'nbre_coups' autorisés
# pendant la partie. Renvoie le nombre de coups restant pour incrémenter le score du joueur.
def deviner_mot(mot_choisi, nbre_coups):
    mot_cache = list(mot_choisi)
    for i, element in enumerate(mot_cache):
        mot_cache[i] = '*'
    print("\n[ {} ]".format(" ".join(mot_cache)))
    liste_lettres = []
    while nbre_coups > 0 and '*' in mot_cache:
        mot_choisi = list(mot_choisi)
        print("\nNombre de coups restants : {}".format(nbre_coups))
        lettre, coup_valide = entrer_lettre()
        for i, element in enumerate(mot_choisi):
            if element == lettre.upper():
                mot_cache[i] = lettre.upper()
        print("\n[ {} ]".format(" ".join(mot_cache)))
        if coup_valide:
            nbre_coups -= 1
            liste_lettres.append(lettre)
            print("Lettres déjà jouées: {}".format(", ".join(liste_lettres)))

    if nbre_coups == 0 and '*' in mot_cache:
        print("\nPERDU! Nombre de coups max atteint")
        mot_choisi = " ".join(mot_choisi)
        print("\nLe mot était : {}".format(mot_choisi.upper()))
        score_tour = 0
    else:
        print("C\'est gagné!! Nombre de points : {}".format(nbre_coups + 1))
        score_tour = nbre_coups+1

    return score_tour

def entrer_nom_joueur(scores):

    nom_joueur = input("\nEntre ton nom pour enregistrer le score: ")
    joueur_existe_deja = True  # Test si joueur est déjà dans la liste des scores
    if not nom_joueur.isalnum():
        print("Nom de joueur non valide")
        return entrer_nom_joueur(scores)
    while joueur_existe_deja:  # Parcours du tableau
        for i in scores.keys():
            while nom_joueur in i:
                try :
                    nom_joueur = input("Nom de joueur déjà existant, essaye un autre nom :")
                    assert len(nom_joueur) > 0
                except AssertionError:
                    print("Nom de joueur non valide")
        joueur_existe_deja = False
    return nom_joueur

# Fonction qui affiche le tableau des meilleurs scores classés dans l'ordre décroissant
# Paramètre d'entrée : 'scores', chargé dans le programme principal depuis le fichier 'donnees'
def affichage_scores(scores):
    print("\nTableau des meilleurs scores :\n")
    liste_score = []
    for i, element in scores.items():
        score_ajouter = (element, i)
        liste_score.append((score_ajouter))
    liste_score.sort(reverse=True)
    for i, elt in enumerate(liste_score):
        print("\n{} : {} pts".format(liste_score[i][1], liste_score[i][0]))

# Fonction qui va lire les scores des joueurs enregistrés dans dictionnaire stocké dans 'donnees'
# Si le fichier 'donnees' n'existe pas, la fonction crée un dictionnaire vide
# La fonction renvoie le dictionnaire 'scores'
def dump_scores():
    try:
        with open('donnees','rb') as fichier:
            fichier_scores = pickle.Unpickler(fichier)
            scores = fichier_scores.load()
    except FileNotFoundError:
            print("Pas de sauvegardes")
            scores = {}
    return scores