# Création avec ()
mon_tuple = (1, 2, 3, 4)
print(type(mon_tuple))

# Accéder à un élément par l'indice.
print(mon_tuple[0])

# Syntaxe : parenthèses facultatives
mon_tuple = 1,
print(type(mon_tuple))

# Convertir une liste en tuple.
ma_liste = [1, 2, 3]
mon_tuple = tuple(ma_liste)

# Inversement
ma_liste = list(mon_tuple)

# unpacking
a, b, c = (1, 2, 3)
print(a, b, c)