import math
import matplotlib.pyplot as plt

class Noeud:
    # 1
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        # Si on ne donne pas d'enfants, on crée une liste vide
        if enfants is None:
            self.enfants = []
        else:
            # Sinon, on utilise la liste fournie
            self.enfants = enfants

    # 2
    def ajouter_enfant(self, noeud_enfant):
        self.enfants.append(noeud_enfant)

    # 3
    def afficher_polonais(self):
        resultat = str(self.valeur)
        for enfant in self.enfants:
            resultat += " " + enfant.afficher_polonais()
        return resultat

     # 5
    def evaluer(self, variables):
        # Cas 1 : Le noeud n'a pas d'enfant. C'est donc un chiffre ou une lettre (x, y)
        if not self.enfants:
            if isinstance(self.valeur, (int, float)):
                return float(self.valeur)
            elif isinstance(self.valeur, str):
                return float(variables[self.valeur])
        
        # Cas 2 : Le noeud a des enfants. C'est donc un opérateur (+, -, *, exp)
        if self.valeur == '+':
            return self.enfants[0].evaluer(variables) + self.enfants[1].evaluer(variables)
        elif self.valeur == '-':
            return self.enfants[0].evaluer(variables) - self.enfants[1].evaluer(variables)
        elif self.valeur == '*':
            return self.enfants[0].evaluer(variables) * self.enfants[1].evaluer(variables)
        elif self.valeur == 'exp':
            return math.exp(self.enfants[0].evaluer(variables))


    # 6
    def tracer(self, variable, valeurs):
        y_valeurs = []
        for val in valeurs:
            # On calcule le résultat pour chaque valeur et on le stocke
            resultat = self.evaluer({variable: val})
            y_valeurs.append(resultat)
        
        # Affichage avec matplotlib
        plt.plot(valeurs, y_valeurs)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.show()
    
            