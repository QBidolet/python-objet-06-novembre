import re
# Module re :
# Permet de manipuler
# des chaines de caractères via des expressions régulières.

# search() : Rechercher un motif dans une chaine de caractère.
exemple = "Python est amusant."
motif = "est"
# Retourne un objet Match s'il trouve une correspondance.
resultat = re.search(motif, exemple)
if resultat:
    print("Une correspondance a été trouvé.")

# Objet Match
print(resultat)
# span : retourne la position : début - fin
print(resultat.span())
# string : la chaine qu'on a passé en paramètre
print(resultat.string)
# group : Affiche le motif
print(resultat.group())

# match(): chercher si le début de la chaine correspond au motif
resultat = re.match("Python", exemple)
if resultat:
    print("Le début correspond.")

# findall() : met dans une liste toutes les correspondances
toutes_correspondances = re.findall("n", exemple)
print(f"{len(toutes_correspondances)}")

# sub : remplace toutes les occurences du motifs par un autre.
remplace = re.sub("amusant", "intéressant", exemple)
print(remplace)

# Conseils:
# Il est conseillé quand vous utilisez du regex d'utiliser
# des chaines de caractère "brute" (raw string) en python
# r"\n"
# Les expressions régulières sont puissantes pour la validation des données
# : emails, numéro de téléphone etc.