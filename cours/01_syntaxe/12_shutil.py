import os
import shutil

# Copier des répertoires et des fichiers.
# Peut aussi les déplacer.
# Peut aussi les renommer en même temps.

# copie simple
src = os.path.join(os.getcwd(), "Images", "dauphin.jpg")
os.makedirs(os.path.join(os.getcwd(), "Images_Backup"), exist_ok=True)
dst = os.path.join(os.getcwd(), "Images_Backup", "dauphin2.jpg")
shutil.copy(src, dst)

# copie récursive
os.makedirs(os.path.join(os.getcwd(), "data"), exist_ok=True)
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
# attention, si le répertoire de dst existe,
# une exception et levée.
shutil.copytree(src, dst)

# suppression récursive
shutil.rmtree(src)

# déplacement
shutil.move(src, dst)