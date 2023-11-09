"""
Parc de Véhicules
Vous êtes chargé de créer une simulation pour un parc de véhicules.
Chaque type de véhicule se déplace de manière différente.
On déplace un véhicule en appelant une méthode "se_deplacer" qui renvoit une chaine de caractère.
Exemple :
 Un avion peut renvoyer "Un avion vole dans le ciel"
 Un bateau peut renvoyer "Un bateau navigue sur l'eau"
 Une voiture [...]

Utiliser le polymorphisme pour permettre à chaque type de véhicule de se déplacer.
Stocker tous les véhicules dans une liste et créer une fonction pour déplacer tous les véhicules de la liste.
"""
class Voiture:
    def se_deplacer(self):
        return "Une voiture roule sur la route."

class Bateau:
    def se_deplacer(self):
        return "Un bateau navigue sur l'eau."

class Avion:
    def se_deplacer(self):
        return "Un avion vole dans le ciel."

def deplacer_vehicules(parc):
    for vehicule in parc:
        print(vehicule.se_deplacer())


parc = []
parc.append(Voiture())
parc.append(Avion())
parc.append(Bateau())

deplacer_vehicules(parc)

