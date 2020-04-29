# -*- coding: utf-8 -*-
# fichier rassemblant toutes les fonctions nécessaires à pendu.py

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
    print("Niveau de jeu :\n\n"
          "1 - Facile, les yeux fermés\n"
          "2 - Normal, mais peut mieux faire\n"
          "3 - Difficile, ça commence à causer\n"
          "4 - Hardcore! Accroche toi Huguette!\n")
    niveau_jeu = input()
    niveau_jeu = int(niveau_jeu)
    if niveau_jeu == 1:
        longueur_mot = 4
    elif niveau_jeu == 2:
        longueur_mot = 6
    elif niveau_jeu == 3:
        longueur_mot = 8
    else:
        longueur_mot = 9

    return longueur_mot

def deviner_mot(mot_choisi, nbre_coups):
    mot_cache = list(mot_choisi)
    for i, element in enumerate(mot_cache):
        mot_cache[i] = '*'
    print("[ {} ]".format(" ".join(mot_cache)))

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

    if nbre_coups == 0 and '*' in mot_cache:
        print("\nPERDU! Nombre de coups max atteint")
        mot_choisi = " ".join(mot_choisi)
        print("\nLe mot était : {}".format(mot_choisi.upper()))
    else:
        print("C\'est gagné!! Nombre de coups restants : {}".format(nbre_coups + 1))
        nbre_coups += 1

    return nbre_coups

def entrer_nom_joueur(scores):
    nom_joueur = input("\nRentre ton nom : ")
    joueur_existe_deja = True  # Test si joueur est déjà dans la liste des scores
    while joueur_existe_deja:  # Parcours du tableau
        for i in scores:
            while nom_joueur in i:
                nom_joueur = input("Nom de joueur déjà existant, essaye un autre nom :")
        joueur_existe_deja = False

    return nom_joueur