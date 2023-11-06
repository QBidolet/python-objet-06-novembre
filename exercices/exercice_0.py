"""
a = 5
b = 6

Codez sans utiliser d'opérateur mathématique autre que le =
pour que a soit égal à 6 et b égal à 5.
"""

# méthode classique
a = 5
b = 6
# temp = a
#
# a = b
# b = temp

# méthode pythonic
a, b = b, a
print(a, b)
