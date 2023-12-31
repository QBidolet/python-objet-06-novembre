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

from tkinter import Tk, Label, Entry, StringVar, Button, Listbox, END, messagebox, TclError, Toplevel


def ajouter_tache():
    tache = nom_tache_var.get()
    if tache:
        listbox_taches.insert(END, tache)


def supprimer_tache():
    try:
        index = listbox_taches.curselection()
        listbox_taches.delete(index)
    except (IndexError, TclError):
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche.")


def sauvegarder_modification(index, nouvelle_tache, fenetre):
    listbox_taches.delete(index)
    listbox_taches.insert(index, nouvelle_tache)
    fenetre.destroy()


def modifier_tache(event):
    index = listbox_taches.curselection()
    tache = listbox_taches.get(index)

    # Nouvelle fenêtre pour éditer la tâche
    edit_fenetre = Toplevel(fenetre)
    edit_fenetre.title("Modifier Tâche")
    modification_var = StringVar()
    entry_modification = Entry(edit_fenetre, textvariable=modification_var)
    entry_modification.pack()
    modification_var.set(tache)
    button_modification = Button(edit_fenetre,
                                 text="Sauvegarder",
                                 command=lambda:
                                 sauvegarder_modification(index, modification_var.get(), edit_fenetre))
    button_modification.pack()


def charger_taches():
    try:
        with open("taches.txt", "r") as fichier:
            for tache in fichier:
                listbox_taches.insert(END, tache)
    except FileNotFoundError:
        pass


def sauvegarder_taches():
    with open("taches.txt", "w") as fichier:
        taches = listbox_taches.get(0, END)
        for tache in taches:
            fichier.write(tache + "\n")
    fenetre.destroy()


def init():
    """
    Construction de la fenêtre.
    """
    global nom_tache_var, listbox_taches, fenetre

    fenetre = Tk()
    fenetre.title("Gestionnaire de Tâches")
    fenetre.geometry("400x400")

    label_titre = Label(fenetre, text="Tache : ")
    label_titre.pack()

    nom_tache_var = StringVar()
    entry_tache = Entry(fenetre, textvariable=nom_tache_var)
    entry_tache.pack()

    listbox_taches = Listbox(fenetre)
    listbox_taches.pack()
    listbox_taches.bind("<Double-1>", modifier_tache)

    button_ajouter = Button(fenetre, text="Ajouter", command=ajouter_tache)
    button_ajouter.pack()

    button_supprimer = Button(fenetre, text="Supprimer", command=supprimer_tache)
    button_supprimer.pack()

    charger_taches()
    fenetre.protocol("WM_DELETE_WINDOW", sauvegarder_taches)
    fenetre.mainloop()


if __name__ == "__main__":
    init()
