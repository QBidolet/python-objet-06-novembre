import sqlite3

# Etablir une connexion
conn = sqlite3.connect("exemple.db")
cursor = conn.cursor()

# Executer des requetes SQL via le cursor.
cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER, nom TEXT)")

# Insertion
cursor.execute("INSERT INTO test (id, nom) VALUES (?, ?)",
               (1, "nom exemple"))

# Récupérer les données
cursor.execute("SELECT * FROM test")
resultats = cursor.fetchall()
for ligne in resultats:
    print(ligne)

# Valider les modifications
conn.commit()
cursor.close()
# Attention à bien Fermer la connexion
conn.close()

# ORM : SQLAlchemy