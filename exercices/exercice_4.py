"""
Vous êtes en charge de modéliser une petite bibliothèque.
La bibliothèque peut avoir plusieurs livres
et chaque livre appartient à une seule bibliothèque.

Définir une classe Livre.
La classe Livre doit avoir au moins deux attributs : titre et auteur.
Elle doit aussi avoir une méthode d'affichage.

Définir une classe Bibliotheque.
La classe Bibliotheque doit avoir un attribut livres
qui est une liste des livres présents dans la bibliothèque.
Ajouter une méthode ajouter_livre pour ajouter un livre à la bibliothèque.
Ajouter une méthode afficher_livres pour afficher tous les livres de la bibliothèque.

Créer une association entre Livre et Bibliotheque :
Chaque Livre doit avoir un attribut bibliotheque
qui fait référence à la Bibliotheque à laquelle il appartient.

Tester votre code :
Instanciez plusieurs livres.
Créez une instance de Bibliotheque.
Ajoutez les livres à la bibliothèque et affichez-les.
"""

class Livre:
    def __init__(self, titre, auteur, bibliotheque=None):
        self.titre = titre
        self.auteur = auteur
        self.bibliotheque = bibliotheque

    def __str__(self):
        return f"{self.titre} par {self.auteur}."

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livre(self):
        for livre in self.livres:
            print(livre)

    def __str__(self):
        resultat = "\n*** BIBLIOTHEQUE ***\n\n"
        for livre in self.livres:
            resultat += livre.__str__() + "\n"
        return resultat


bibliotheque = Bibliotheque()
livre_1 = Livre(titre="1984", auteur="George Orwell", bibliotheque=bibliotheque)
livre_2 = Livre(titre="Le Meilleur des mondes", auteur="Aldous Huxley", bibliotheque=bibliotheque)
livre_3 = Livre(titre="Voyage au bout de la nuit", auteur="Celine", bibliotheque=bibliotheque)
bibliotheque.ajouter_livre(livre_1)
bibliotheque.ajouter_livre(livre_2)
bibliotheque.ajouter_livre(livre_3)

print(bibliotheque)