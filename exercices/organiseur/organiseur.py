"""
Construire un organiseur de fichier
selon le dictionnaire donné.
Le programme doit scanner le dossier et devra
créer un dossier correspondant au type de fichier
et déplacer celui-ci à l'intérieur.
Exemple : Dans mon dossier A TRIER j'ai
une fichier de type PDF, je crée un répertoire PDF
et je déplace le fichier à l'intérieur.

BONUS :
Trouver les 3 façons de faire pour parcourir les fichiers d'un dossier.
"""
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

# listdir
chemin = os.path.join(os.getcwd(), "A TRIER")

for fichier in os.listdir(chemin):
    nom, extension = os.path.splitext(fichier)
    print(nom, extension)
    for cle, valeur in folder_dict.items():
        if extension in valeur:
            print(f"Le dossier a crée est {cle}")

# méthode 2


# méthode 3