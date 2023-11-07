# 4 modes d'ouvertures
# r : pour lire
# w : pour écrire et écraser le contenu
# x : pour écrire si et seulement si le fichier est inexistant.
# a : ajouter à la suite. (append) Crée le fichier s'il n'existe pas.

# méthode classique
fichier = open("todo.txt", "rt")
contenu = fichier.read()
print(contenu)
fichier.close()

# méthode pythonic avec with
with open("todo.txt", "rt") as fichier:
    contenu = fichier.read()
    print(contenu)

# Ecriture avec w, x ou a
with open("todo.txt", "a") as fichier:
    fichier.write("Une nouvelle ligne.\n")

print("#"*25)
with open("todo.txt", "r") as fichier:
    for ligne in fichier.readlines():
        print(ligne)


# seek
print("#" * 25)
fichier = open("todo.txt", "r")
print(fichier.tell())
print(fichier.read())
print(fichier.tell())
fichier.seek(5)
print(fichier.tell())
print(fichier.read())

fichier.close()

# writelines
fruits = ["pomme", "banane"]
with open("todo.txt", "w") as fichier:
    fichier.writelines(fruits)