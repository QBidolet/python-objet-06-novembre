class Voiture:
    def __init__(self, couleur="Verte", marque="Tesla"):
        self.couleur = couleur
        self.marque = marque

    def klaxonner(self):
        print("tut tut")

    def repeindre(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return (f"Je suis une voiture {self.couleur} de marque "
                f"{self.marque}.")

    def __eq__(self, obj):
        return self.marque == obj.marque and self.couleur == obj.couleur