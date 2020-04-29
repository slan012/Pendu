# -*- coding: utf-8 -*-
# fichier rassemblant toutes les fonctions nécessaires à pendu.py

# fonction qui vérifie si la lettre tapée par le joueur n'est ni un entier ni un flottant
def entrer_lettre():
    lettre_chiffre = True
    lettre = 'None'
    while lettre_chiffre or len(lettre) != 1:
        try:
            lettre = input("Lettre : ")
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