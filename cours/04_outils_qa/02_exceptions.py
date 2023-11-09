# Lever une exception
# nombre = input("Veuillez entrer un entier.")
# try:
#     nombre = int(nombre)
# except ValueError:
#     print("Veuillez entrer un nombre valide.")
# else:
#     # Execution que s'il n'y a pas eu d'exception.
#     print(nombre)

# # Gérer plusieurs exceptions
# try:
#     numerateur = float(input("Veuillez entrer un numérateur."))
#     denominateur = float(input("Veuillez entrer un denominateur."))
#     resultat = numerateur/denominateur
# # Première manière, on gère tout dans le même except.
# # except (ValueError, ZeroDivisionError):
# #     print("Veuillez entrer des nombres valides.")
# except ValueError:
#     print("Veuillez entrer des nombres valides.")
# except ZeroDivisionError:
#     print("Le denominateur ne peut pas être 0.")
# else:
#     print(resultat)

# Lever une exception avec Raise
# raise Exception("Vous ne pouvez pas effectuer cette action.")
raise ValueError

# https://docs.python.org/fr/3/library/exceptions.html
# Sentry