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

chemin_a_trier = os.path.join(os.getcwd(), "A TRIER")

# listdir
# liste_fichiers = os.listdir(chemin_a_trier)
# for fichier in liste_fichiers:
#     _, extension = os.path.splitext(fichier)
#     for cle, valeur in folder_dict.items():
#         if extension in valeur:
#             chemin_dossier = os.path.join(os.getcwd(), cle)
#             os.makedirs(chemin_dossier, exist_ok=True)
#             chemin_fichier = os.path.join(chemin_a_trier, fichier)
#             shutil.copy2(chemin_fichier, chemin_dossier)

# scandir
# for element in os.scandir(chemin_a_trier):
    # if element.is_file():
    #     _, extension = os.path.splitext(element.name)
    #     for nom_repertoire, liste_extension in folder_dict.items():
    #         if extension in liste_extension:
    #             chemin_dossier = os.path.join(os.getcwd(), nom_repertoire)
    #             os.makedirs(chemin_dossier, exist_ok=True)
    #             chemin_fichier = os.path.join(chemin_a_trier, element.name)
    #             shutil.copy2(chemin_fichier, chemin_dossier)

# os.walk
for repertoire_en_cours, sous_repertoires, fichiers in os.walk(chemin_a_trier):
    for fichier in fichiers:
        _, extension = os.path.splitext(fichier)
        for nom_repertoire, liste_extension in folder_dict.items():
            if extension in liste_extension:
                chemin_dossier = os.path.join(os.getcwd(), nom_repertoire)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_fichier = os.path.join(chemin_a_trier, fichier)
                shutil.move(chemin_fichier, chemin_dossier)