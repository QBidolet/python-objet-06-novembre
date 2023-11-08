from voiture import Voiture


class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse

    def __str__(self):
        return (f"Je suis une voiture de course de vitesse {self.vitesse}"
                f", de couleur {self.couleur} et de marque {self.marque}")