"""
Vous êtes le propriétaire d'une ferme numérique.
Vous souhaitez modéliser les animaux de votre ferme et leurs interactions
avec les installations de la ferme.

Créer une classe de base Animal avec :
Une méthode __init__ qui prend un nom.
Une méthode faire_du_bruit().

Créer deux classes dérivées Vache et Poule qui :
Implémentent la méthode faire_du_bruit().
Ont une méthode manger() qui affiche ce qu'ils mangent.

Une classe Ferme avec :
Un attribut animaux qui est une liste des animaux de la ferme.
Une méthode ajouter_animal() pour ajouter un animal à la ferme.
Une méthode faire_le_tour() qui fait faire du bruit à chaque animal.

-- Tester votre code --
Instancier plusieurs Vache et Poule.
Créer une instance de Ferme et y ajouter les animaux créés.
Utiliser la méthode faire_le_tour() pour simuler un tour de la ferme.

"""


class Animal:
    def __init__(self, nom):
        self.nom = nom

    def faire_du_bruit(self):
        print(f"{self.nom} fait du bruit.")

    def manger(self):
        print(f"{self.nom} mange ...")


class Vache(Animal):
    # def __init__(self, nom):
    #     Animal.__init__(self, nom)
    def faire_du_bruit(self):
        print(f"{self.nom} dit Meuh !")

    def manger(self):
        print(f"{self.nom} mange de l'herbe.")


class Poule(Animal):
    def faire_du_bruit(self):
        print(f"{self.nom} dit Cot Cot !")

    def manger(self):
        print(f"{self.nom} mange des graines.")


class Ferme:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def faire_le_tour(self):
        for animal in self.animaux:
            animal.faire_du_bruit()

# Instanciation des animaux
marguerite = Vache("Marguerite")
cotcot = Poule("Cotcot")
rosline = Vache("Rosline")
poulette = Poule("Poulette")

# Instanciation de la ferme
ferme = Ferme()

# Ajouter les animaux dans la ferme
ferme.ajouter_animal(marguerite)
ferme.ajouter_animal(cotcot)
ferme.ajouter_animal(rosline)
ferme.ajouter_animal(poulette)

# On vérifie que tout fonctionne !
ferme.faire_le_tour()