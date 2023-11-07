"""
Gestionnaire de Contacts

Écrire un script Python qui permet de créer, afficher, et gérer un carnet d'adresses simple.
Écrire des docstrings en haut du fichier et des fonctions
pour décrire l'utilisation du script.

Créer un dictionnaire global pour stocker les contacts (nom comme clé, numéro de téléphone comme valeur).

Écrire une fonction ajouter_contact(nom, numero) pour ajouter un nouveau contact au carnet d'adresses.
Écrire une fonction afficher_contacts() qui affiche tous les contacts et leurs numéros de téléphone.
Écrire une fonction sauvegarder_contacts() qui écrit le carnet d'adresses actuel dans un fichier.
Écrire une fonction charger_contacts() qui lit les contacts à partir d'un fichier et les charge dans le dictionnaire des contacts.

Utiliser la structure conditionnelle if/elif/else pour permettre à l'utilisateur de choisir entre ajouter un contact, afficher les contacts, sauvegarder ou charger les contacts.
"""
#
# """
# GESTIONNAIRE DE CONTACTS
# 1 - Ajouter un contact
# 2 - Afficher les contacts
# 3 - Sauvegarder les contacts
# 4 - Charger les contacts
# 5 - Quitter
# """

contacts = {}

def ajouter_contacts(nom, numero):
    contacts[nom] = numero

def afficher_contacts():
    print("*** CONTACTS ***")
    print("Nom | Telephone")
    for nom, telephone in contacts.items():
        print(f"{nom} | {telephone}")


def sauvegarder_contacts():
    with open("contacts.txt", "w") as fichier:
        for nom, telephone in contacts.items():
            fichier.write(nom + "," + telephone)


def charger_contacts():
    # contacts.clear()
    with open("contacts.txt", "r") as fichier:
        for ligne in fichier.readlines():
            nom, telephone = ligne.strip().split(",")
            contacts[nom] = telephone
def menu():
    while True:
        print("\nGestionnaire de contacts")
        print("1: Ajouter contacts")
        print("2: Afficher contacts")
        print("3: Sauvegarder contacts")
        print("4: Charger contacts")
        print("5: Quitter")

        choix = input("Choisissez une option :\n")
        if choix == "1":
            nom = input("Veuillez entrer un nom de contact.\n")
            telephone = input("Veuillez entrer un téléphone.\n")
            ajouter_contacts(nom, telephone)
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            sauvegarder_contacts()
        elif choix == "4":
            charger_contacts()
        else:
            print("Fin du programme.")
            break


menu()