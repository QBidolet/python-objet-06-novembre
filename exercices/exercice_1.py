"""
Ecrire un programme qui demande à l'utilisateur de saisir une vitesse en miles/heure.
Vous devez afficher cette vitesse en km/h et m/s.
Vous devez également réinviter votre utilisateur à saisir une nouvelle valeur
et "boucler" de cette manière.
Indication pour la conversion :
    - miles/heure à m/s, il faut diviser par 2.237.
    - miles/heure à km/h, il faut multiplier par 1.609
"""
liste_continuer = ["oui", "yes", "y", "o"]
continuer = "oui"

while continuer in liste_continuer:
    saisie = input("Saisissez une vitesse en miles/heure.\n")
    vitesse = float(saisie)
    m_s = vitesse / 2.237
    km_h = vitesse * 1.609
    print(f"{km_h} km/h\n{m_s} m/s.")
    continuer = input(f"\nVoulez-vous continuer ?({'/'.join(liste_continuer)})\n")
    continuer = continuer.lower()