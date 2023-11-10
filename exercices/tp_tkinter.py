"""
Créez une application de gestion de tâches simple
L'utilisateur doit être capable d'ajouter des tâches dans une liste,
de les sélectionner et de les supprimer.

Utilisez un Frame comme conteneur principal.
Ajoutez un Label en haut de la fenêtre avec le titre de votre application
(ex. "Gestionnaire de Tâches").

Ajout de Tâches :
Utilisez un Entry pour permettre à l'utilisateur de saisir le nom d'une tâche.
Ajoutez un Button "Ajouter" qui, lorsqu'il est cliqué,
ajoute la tâche dans une Listbox.

Affichage des Tâches :
Utilisez une Listbox pour afficher les tâches ajoutées.

Suppression de Tâches :
Ajoutez un Button "Supprimer"
qui permet de supprimer la tâche sélectionnée dans la Listbox.

Gestion de l'Absence de Sélection :
Si "Supprimer" est cliqué sans sélectionner de tâche,
affichez un message à l'aide de messagebox.

Bonus :
Sauvegarde et Chargement des Tâches :
Ajoutez la capacité de sauvegarder les tâches dans un fichier lors de la fermeture de l'application et de les charger au démarrage.
Utilisez des fichiers texte pour la stocker les données.

Modification des Tâches Existantes :
Permettez à l'utilisateur de double-cliquer sur une tâche dans la Listbox pour la modifier.
Ouvrez une nouvelle fenêtre de dialogue pour l'édition.
"""

import tkinter as tk
from tkinter import messagebox


# Fonction pour ajouter une tâche
def ajouter_tache():
    tache = entry_tache.get()
    if tache:
        listbox_taches.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Vous devez entrer une tâche.")


# Fonction pour supprimer une tâche sélectionnée
def supprimer_tache():
    try:
        index = listbox_taches.curselection()[0]
        listbox_taches.delete(index)
    except IndexError:
        messagebox.showwarning("Attention", "Vous devez sélectionner une tâche.")


# Fonction pour sauvegarder les tâches dans un fichier
def sauvegarder_taches():
    with open('taches.txt', 'w') as f:
        taches = listbox_taches.get(0, tk.END)
        for tache in taches:
            f.write(tache + "\n")
    fenetre.destroy()


# Fonction pour charger les tâches à partir d'un fichier
def charger_taches():
    try:
        with open('taches.txt', 'r') as f:
            for tache in f:
                listbox_taches.insert(tk.END, tache.strip())
    except FileNotFoundError:
        pass


# Fonction pour modifier une tâche existante
def modifier_tache(event):
    try:
        index = listbox_taches.curselection()[0]
        tache = listbox_taches.get(index)

        # Fenêtre de modification
        edit_window = tk.Toplevel(fenetre)
        edit_window.title("Modifier Tâche")
        tk.Entry(edit_window, textvariable=nom_var).pack()
        nom_var.set(tache)
        tk.Button(edit_window, text="Sauvegarder",
                  command=lambda: sauvegarder_modification(index, edit_window)).pack()

    except IndexError:
        pass


# Fonction pour sauvegarder la modification d'une tâche
def sauvegarder_modification(index, window):
    nouvelle_tache = nom_var.get()
    listbox_taches.delete(index)
    listbox_taches.insert(index, nouvelle_tache)
    window.destroy()


# Initialisation de la fenêtre Tkinter
def init():
    global fenetre, entry_tache, listbox_taches, nom_var

    fenetre = tk.Tk()
    fenetre.title("Gestionnaire de Tâches")
    fenetre.geometry('300x300')

    nom_var = tk.StringVar()
    recherche_var = tk.StringVar()

    tk.Label(fenetre, text="Tâche :").pack()
    entry_tache = tk.Entry(fenetre, textvariable=nom_var)
    entry_tache.pack()

    tk.Button(fenetre, text="Ajouter Tâche", command=ajouter_tache).pack()
    tk.Button(fenetre, text="Supprimer Tâche", command=supprimer_tache).pack()

    listbox_taches = tk.Listbox(fenetre)
    listbox_taches.pack()

    listbox_taches.bind("<Double-1>", modifier_tache)

    charger_taches()
    fenetre.protocol("WM_DELETE_WINDOW", sauvegarder_taches)
    fenetre.mainloop()


if __name__ == "__main__":
    init()