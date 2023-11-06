# echapper (escape) avec \
ma_phrase = "J'ai 30 ans."
ma_phrase = 'J\'ai 30 ans.'

print(ma_phrase)

# multiligne
ma_phrase = """J'ai 30 ans
et je suis content."""

print(ma_phrase)

# concaténer avec +
prenom = "Quentin"
nom = "BIDOLET"
print("Je m'appelle " + prenom + " " + nom + ".")

# version python 2
ma_phrase = "Je m'appelle %s %s." % (prenom, nom)
print(ma_phrase)

# version python 3
ma_phrase = "Je m'appelle {0} {1}.".format(prenom, nom)
print(ma_phrase)

# version pythonic
ma_phrase = f"Je m'appelle {prenom} {nom}."
print(ma_phrase)

# dupliquer
print("#"*25)

alphabet = "abcdefghij"
# extraction de chaine de caractère
# [ start : end : step ]
# [start :] : démarre à l'indice start jusqu'à la fin
print(alphabet[3:])
# [start : end ]
print(alphabet[3:6])
# [start : end : step ]
print(alphabet[::2])
print(alphabet[::-1])
print(alphabet[:-2])