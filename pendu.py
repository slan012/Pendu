# -*- coding: utf-8 -*-


# début de partie le joueur donne son nom
# si aucun score enregistré -> score = 0 pts => {'nom_joueur' : 0}
mot ="test"
lettre = 'a'
mot = list(mot)
print(mot)


# Vérifie si une 'lettre' est dans le 'mot' et affiche le mot avec des étoiles sur les lettres qui n'y sont pas

def verifier_lettre(lettre, mot) 
	for i, element in enumerate(mot) :
		if element != lettre :
			mot[i] = '*'
	mot = "".join(mot)
	print("[ {} ]".format(mot))
	


	

# mot de 8 lettres max choisi au hasard dans une liste
# joueur saisi une lettre par tour (vérifier que c'est bien le cas (len(mot))

# si lettre est dans le mot 
	# afficher la (ou les) lettre(s) dans le mot à la bonne place
	# mettre etoiles à la place des autres lettres
	
# 8 coups maximum -> sinon partie perdu
# si mot trouvé -> score += nbre de coups restants