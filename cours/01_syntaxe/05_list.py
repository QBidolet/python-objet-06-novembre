fruits = ["pomme", "banane", "cerise"]
print(fruits)
une_liste = ["pomme", 5.0, True, ["kiwi"]]
print(une_liste)

# Sélection sur un élément
print(une_liste[0])
print(une_liste[2])
print(une_liste[3])

print(type(fruits))

# Sélection sur plusieurs éléments
print(une_liste[0:2])

# Ajouter un élément
une_liste.append(4)
print(une_liste)

une_liste.insert(0, -99)

print(une_liste)

# Compter le nombre d'occurrence d'une valeur.
print(une_liste.count("pomme"))

# Afficher la longueur de la liste.
print(len(une_liste))

# Suppression à partir de la valeur
une_liste.append(-99)
une_liste.remove(-99) # Attention : ne supprime que la première occurrence.
print(une_liste)

# Supprimer avec del par index
del une_liste[0]
print(une_liste)

# gestion mémoire
a = [1, 2, 3, 4, 5]
b = a
print(id(a), id(b))
a[0] = 0
print(b)

# opérateur d'appartenance in
# fonctionne si l'objet est un itérable.
if 0 in a:
    print("0 est dans a.")

# trier
# reverse = True pour inverser le trie.
a.sort(reverse=True)
print(a)

# passer d'une liste à un string et inversement
ma_liste = ["oui", "yes", "ok"]
print("/".join(ma_liste))

ma_chaine = 'oui:yes:ok'
ma_liste = ma_chaine.split(':')
print(ma_liste)

