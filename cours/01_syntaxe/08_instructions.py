# conditionnelle

prenom = "Quentin"
age = 29

if prenom == "Julien":
    print("Il s'appelle Julien")
elif age == 30:
    print("Il a 30 ans.")
else:
    print("Autre.")

# Boucles
# for

for caractere in prenom:
    print(caractere)

for indice, caractere in enumerate(prenom):
    print(indice, caractere)

# range(start, end, step)
# ou
# range(end)
for indice in range(1, 6, 2):
    print(indice)

for indice in range(6):
    print(indice)

# while
i = 0
while i < 6:
    print("hello " + str(i))
    if i != 5:
        break  # sort de la boucle
        continue # va retester la condition de sortie et passer au tour suivant
    i += 1
