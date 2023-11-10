from tkinter import Tk, Label, Entry, Button, StringVar
import sqlite3


def create_database():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(nom TEXT, telephone TEXT);")
    connection.commit()
    cursor.close()
    connection.close()
    # SQL Alchemy est un ORM.


def insert():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contacts VALUES (?,?)", (nom_var.get(),
                                                         telephone_var.get()))

    connection.commit()
    cursor.close()
    connection.close()


def show():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts;")
    for element in cursor.fetchall():
        nom, telephone = element
        print(nom, telephone)

    connection.commit()
    cursor.close()
    connection.close()


def init():
    # Création d'une fenêtre.
    fenetre = Tk()
    fenetre.geometry('410x450')
    fenetre.title("Annuaire")
    fenetre.configure(background="powder blue")

    # Créer des widgets
    name_label = Label(fenetre, text="Nom :")
    name_label.place(x=0, y=0)

    telephone_label = Label(fenetre, text="Téléphone :")
    telephone_label.place(x=0, y=30)

    # Création des champs de saisie (input c'est Entry sur tkinter).
    global nom_var
    global telephone_var
    nom_var, telephone_var = StringVar(), StringVar()
    nom_entry = Entry(fenetre, width=20, textvar=nom_var)
    nom_entry.place(x=80, y=0)

    telephone_entry = Entry(fenetre, width=20, textvar=telephone_var)
    telephone_entry.place(x=80, y=30)

    # création des boutons
    bouton_insertion = Button(fenetre, text="Insérer", command=insert)
    bouton_insertion.place(x=80, y=100)

    bouton_afficher = Button(fenetre, text="Afficher", command=show)
    bouton_afficher.place(x=130, y=100)
    fenetre.mainloop()


if __name__ == "__main__":
    create_database()
    init()