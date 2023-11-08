from voiture import Voiture
from voiture_de_course import VoitureDeCourse

voiture = Voiture("Noir", "Tesla")
print(voiture)

voiture_2 = VoitureDeCourse("Verte", "Tesla", 350)
print(voiture_2)
print(voiture_2.couleur, voiture_2.marque, voiture_2.vitesse)

compte_dupont = CompteBancaire("DUPONT", 10000)
compte_dupont.ajouter(100)