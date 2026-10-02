from noeud import Noeud

# 4
noeud_add = Noeud('+', [Noeud(2), Noeud('y')])
noeud_exp = Noeud('exp', [noeud_add])

# Test de la question 4 (Affichage polonais)
print("Affichage polonais :", noeud_exp.afficher_polonais())

# Test de la question 5 (Évaluation)
valeurs_variables = {'y': 3.0}
print("Résultat du calcul :", noeud_exp.evaluer(valeurs_variables))

# Test de la question 6 (Graphique)

liste_valeurs = [0, 1, 2, 3, 4]
noeud_exp.tracer('y', liste_valeurs)