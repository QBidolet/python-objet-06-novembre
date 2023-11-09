"""
Vous êtes chargé de créer une application de bibliothèque numérique.
Vous devez modéliser les utilisateurs, les livres,
les auteurs, et la gestion des prêts.
L'application doit permettre d'ajouter des livres,
 de les emprunter et de les retourner.

Classe Personne:
Attributs : nom, prénom, date de naissance.
Méthode __str__() qui retourne une chaîne de caractères avec le nom complet de la personne.

Classe Utilisateur héritant de Personne:
Attributs supplémentaires : identifiant utilisateur,
liste des livres empruntés.
Méthodes pour emprunter un livre, retourner un livre,
et lister les livres empruntés.

Classe Auteur héritant de Personne:
Attribut supplémentaire : liste des livres écrits.
Méthode pour ajouter un livre à la liste des livres écrits.

Classe Livre:
Attributs : titre, auteur (Auteur), année de publication,
 identifiant unique, statut (disponible ou emprunté).
Méthode __str__() pour retourner une description du livre.

Classe Bibliothèque:
Attribut : catalogue : liste de livres.
Méthodes pour ajouter un livre au catalogue,
 emprunter un livre (en changeant son statut), et retourner un livre.


-- Interaction et Gestion des Prêts --
Créer des instances de Utilisateur, Auteur, et Livre.
Ajouter des livres au catalogue de la bibliothèque.
Réaliser des opérations d'emprunt et de retour de livre.
Afficher l'état actuel du catalogue et les livres empruntés par un utilisateur.

Vous pouvez utilisez des docstrings pour documenter vos classes et méthodes.
Testez votre application en créant au moins 3 utilisateurs, 2 auteurs et 3 livres.
"""


class Personne:
    def __init__(self, nom, prenom, date_de_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Utilisateur(Personne):
    def __init__(self, nom, prenom, date_de_naissance, identifiant):
        super().__init__(nom, prenom, date_de_naissance)
        self.identifiant = identifiant
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        self.livres_empruntes.append(livre)
        livre.statut = "emprunté"

    def retourner_livre(self, livre):
        self.livres_empruntes.remove(livre)
        livre.statut = "disponible"

    def lister_livres_empruntes(self):
        for livre in self.livres_empruntes:
            print(livre)


class Auteur(Personne):
    def __init__(self, nom, prenom, date_de_naissance):
        super().__init__(nom, prenom, date_de_naissance)
        self.livres_ecrits = []

    def ajouter_livre_ecrit(self, livre):
        self.livres_ecrits.append(livre)


class Livre:
    def __init__(self, titre, auteur, annee_publication, identifiant):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.identifiant = identifiant
        self.statut = "disponible"

    def __str__(self):
        return f"{self.titre} par {self.auteur} publié en {self.annee_publication}"


class Bibliotheque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self, livre):
        self.catalogue.append(livre)

    def emprunter_livre(self, identifiant, utilisateur):
        for livre in self.catalogue:
            if livre.identifiant == identifiant:
                if livre.statut == "disponible":
                    utilisateur.emprunter_livre(livre)
                    print(f"Le livre {livre} a été emprunté par {utilisateur}")
                else:
                    print(f"Le livre {livre} n'est pas disponible.")

    def retourner_livre(self, identifiant, utilisateur):
        for livre in utilisateur.livres_empruntes:
            if livre.identifiant == identifiant:
                utilisateur.retourner_livre(livre)
                print(f"Livre {livre.titre} retourné par {utilisateur}.")

    def afficher_catalogue(self):
        print("*** CATALOGUE ***")
        for livre in self.catalogue:
            print(str(livre) + " - Disponibilité : " + livre.statut)


utilisateur_1 = Utilisateur("DUPONT", "Jean", "01/01/1980", "I458")
auteur_1 = Auteur("Rowling", "J.K", "31/07/1965")
auteur_2 = Auteur("Tolkien", "J.R.R", "31/07/1965")

livre_1 = Livre("Harry Potter 1", auteur_1, 1997, "L0152")
livre_2 = Livre("Le Seigneur des Anneaux", auteur_2, 1954, "L0153")

auteur_1.ajouter_livre_ecrit(livre_1)
auteur_2.ajouter_livre_ecrit(livre_2)

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre_1)
bibliotheque.ajouter_livre(livre_2)

print("#" *25)
# Emprunt
bibliotheque.emprunter_livre("L0152", utilisateur_1)
bibliotheque.emprunter_livre("L0153", utilisateur_1)

bibliotheque.afficher_catalogue()

print("#" *25)
bibliotheque.retourner_livre("L0152", utilisateur_1)
bibliotheque.retourner_livre("L0153", utilisateur_1)

bibliotheque.afficher_catalogue()
