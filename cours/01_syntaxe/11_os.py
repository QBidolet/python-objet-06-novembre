import os

# A EVITER : chemin absolu
chemin = "D:/Quentin/Projects/Site/"

# A utiliser : créer des chemins avec os.path.join
chemin_fichier = os.path.join(os.getcwd(), "repertoire", "dauphin.jpg")
print(chemin)

# vérifier l'existence d'un fichier
print(os.path.isfile(chemin_fichier))

# créer un dossier
os.makedirs("Images", exist_ok=True)

# changer le répertoire courant
chemin = os.path.join(os.getcwd(), "Images")
os.chdir(chemin)

# vérifier l'existence d'un dossier
print(os.path.isdir(chemin))

# Récupérer nom et extension à partir d'un nom de fichier
nom, extension = os.path.splitext("fichier.txt")
print(nom, extension)

# lister les dossiers et fichiers d'un répertoire
print(os.listdir(chemin))