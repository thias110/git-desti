"""Niveau 2 : Structures de données

Objectif : apprendre à manipuler listes, dictionnaires, fonctions.

Listes

Crée une liste de 5 prix d’actions (par ex. [10, 12, 8, 14, 9]).

Calcule et affiche :

la moyenne des prix

le prix maximum

le prix minimum



"""

actions = [10, 12, 7, 9]
resultatmoyenne = 0
resultatnax = 0
resultatmin = 0


"""Traitement..."""
i = 0
while i < len(actions) - 1:

    resultatmoyenne += actions[i]
    i += 1

resultatmoyenne = resultatmoyenne / len(actions)


e = 0

while e < len(actions) - 1:

    if actions[e] < actions[e + 1]:
        resultatnax = actions[e]
        actions[e] = actions[e + 1]
    e += 1

o = 0
while o < len(actions) - 1:

    if actions[o] > actions[o + 1]:
        resultatmin = actions[o]
        actions[o] = actions[o + 1]
    o += 1


"""Final"""

print("La moyenne du prix des actions est de " + str(resultatmoyenne))
print("Le minimum du prix des actions est de " + str(resultatnax))
print("Le maximum du prix des actions est de " + str(resultatmin))
"""

Dictionnaires

Crée un dictionnaire portefeuille avec des actions et leurs quantités, ex :

{"AAPL": 10, "TSLA": 5, "AMZN": 2}


Ajoute une nouvelle action.

Affiche toutes les clés (les noms des actions).

Fonctions

Écris une fonction rendement(prix_achat, prix_vente) qui retourne le rendement en % :

rendement = (prix_vente - prix_achat) / prix_achat * 100"""

"""Initialisation..."""

Nasdaq = {'APPL' : 10, "AMZN":25,"NVDIA":13,"APPL":21}

"""Traitement..."""

def Rendement(prixVente, prixAchat):
     Rendementval = 0
     Rendementval=(prixVente-prixAchat)/prixAchat*100
     return Rendementval

resultat = Rendement(11,12)


print("Ton rendement est de "+str(resultat) +"%")


