import sys

print("Nom du script : " + sys.argv[0])

# Itérer sur les arguments
for i in range(1, len(sys.argv)):
    print(f"Argument {i} : {sys.argv[i]}")

# python 01_sys.py BIDOLET 25 38

if len(sys.argv) > 1:
    print("Au moins un argument a été fourni.")
else:
    print("Aucun argument.")

# Exemple script pour se connecter à un serveur.
# Il faut fournir nom d'utilisateur et mot de passe.

if len(sys.argv) == 3:
    username = sys.argv[1]
    password = sys.argv[2]
    print(f"Nom d'utilisateur : {username}, mot de passe : {password}")
else:
    print("Veuillez fournir un nom d'utilisateur et un mot de passe.")