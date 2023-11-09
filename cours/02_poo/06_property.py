class Personne:
    def __init__(self, nom, age):
      self.__nom = nom
      self.__age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if isinstance(value, str):
            self.__nom = value
        else:
            # lever une exception
            # ou afficher un message
            print("Valeur invalide.")

personne = Personne("BIDOLET", 15)
print(personne.nom)
personne.nom = "DUPONT"
print(personne.nom)

personne.nom = []