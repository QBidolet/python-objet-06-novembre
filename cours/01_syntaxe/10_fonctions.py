def do_nothing():
    pass


do_nothing()


def somme(a, b):
    return a + b


# Paramètres positionnels
resultat = somme(1, 2)
print(resultat)

# Paramètres nommés
resultat = somme(b=2, a=1)
print(resultat)


# Une procédure est une fonction qui ne retourne pas de resultat.
def menu(entree="Choux", plat="Steak-frites", dessert="Mousse au chocolat"):
    print(f"Entrée : {entree}\n"
          f"Plat : {plat}\n"
          f"Dessert : {dessert}\n")


menu()

print("Un mot.", "Un autre mot.",
      "Un mot.", "Un autre mot.",
      "Un mot.", "Un autre mot.",
      sep=" ", end="\n")


# *args
# Cela va "packer" toutes les paramètres positionnels
# qu'on lui donne dans un tuple.
def print_2(*args):
    for arg in args:
        print(arg, end="")


def somme(*args):
    resultat = 0
    for arg in args:
        resultat += arg
    return resultat


print(somme(1, 2, 3, 4, 5, 6, 7, 8, 9))


# **kwargs : Va "packer" tous les paramètres nommés
# dans un dictionnaire.
def menu(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle.capitalize()}: {valeur}")


print('#' * 25)
menu(entree="Choux", plat="Steak-frites", entremet="Glace",
     dessert="Mousse au chocolat")

# fonctions anonymes
# map
print("#" * 25)
liste = [1, 2, 3, 4]

# def double(nombre):
#     return nombre * 2


mon_map = map(lambda nombre: nombre * 2, liste)
print(list(mon_map))

# filter
mon_filter = filter(lambda nombre: nombre % 2 == 0, liste)
print(list(mon_filter))

# fonctions génératrices
print("#" * 25)

for i in range(6):
    print(i)


def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1


for i in range_2(6):
    print(i)
