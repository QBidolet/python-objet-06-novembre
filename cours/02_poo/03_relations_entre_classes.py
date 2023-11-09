# Relation Un-à-Un
# Chaque instance d'une classe est associée à une
# unique instance d'une autre classe.


class User:
    def __init__(self, profile):
        self.profile = profile


class Profile:
    def __init__(self, user):
        self.user = user


user_profile = Profile(None)
user = User(user_profile)
user_profile.user = user


# Un-à-Plusieurs (1:n)
# Une instance d'une classe est associée à plusieurs instances d'une autre classe.
# Exemple : Un professeur a plusieurs élèves.
# Plusieurs-à-un (n:1)
# Plusieurs instances d'une classe sont associées à une seule instance d'une autre classe.

class Professeur:
    def __init__(self):
        self.eleves = []


class Eleve:
    def __init__(self, professeur):
        self.professeur = professeur
        professeur.eleves.append(self)


professeur = Professeur()
eleve_1 = Eleve(professeur)
eleve_2 = Eleve(professeur)

print(len(professeur.eleves))


# Plusieurs-à-plusieurs
# Les instances d'une classe sont associées à plusieurs instances d'une autre classe
# et vice-versa.
# Exemple : Des étudiants peuvent s'inscrire à plusieurs cours
# et chaque cours peut avoir plusieurs étudiants.

class Cours:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        etudiant.ajouter_cours(self)


class Etudiant:
    def __init__(self):
        self.cours = []

    def ajouter_cours(self, cours):
        self.cours.append(cours)

cours_1 = Cours()
cours_2 = Cours()
etudiant = Etudiant()

cours_1.ajouter_etudiant(etudiant)
cours_2.ajouter_etudiant(etudiant)
# etudiant.ajouter_cours(cours_1)
# etudiant.ajouter_cours(cours_2)

# Relation unidirectionnelle
# Seule une classe a une référence vers l'autre.

# Relation bidirectionnelle
# Les deux classes ont une référence l'une à l'autre.

# Navigabilité
# La capacité d'accéder aux instances d'une autre classe.