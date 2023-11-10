import tkinter as tk
from tkinter import messagebox

# Créer une fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter")
root.geometry("500x500")
root.configure(background="powder blue")

# Frame : Un conteneur pour d'autres widgets
frame = tk.Frame(root)
frame.pack()

# Widgets
button = tk.Button(frame, text="Cliquez-ici",
                   command=lambda: messagebox.showinfo("Information",
                                                       "Hello World!")
                   )
button.pack()

# Entry
entry = tk.Entry(frame)
entry.pack()

# ListBox
listbox = tk.Listbox(frame)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.pack()

# Text
text = tk.Text(frame, height=5, width=30)
text.pack()

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Canvas
canvas = tk.Canvas(frame, bg="white", height=100, width=100)
canvas.pack(side="left")


def on_keypress(event):
    print("Touche pressée :", event.char)


root.bind("<KeyPress>", on_keypress)

def ouvrir_nouvelle_fenetre():
    nouvelle_fenetre = tk.Toplevel(root)
    nouvelle_fenetre.title("Nouvelle fenêtre")
    label = tk.Label(nouvelle_fenetre, text="Ceci est une nouvelle fenêtre")
    label.pack(side="left")

bouton_nouvelle_fenetre = (
    tk.Button(frame, text="Nouvelle fenêtre", command=ouvrir_nouvelle_fenetre))
bouton_nouvelle_fenetre.pack(side="left")

# pack : les uns après les autres. pack(side="left") (top/bottom/left/right)
# grid : en grille, exemple : grid(row=1, column=0)
# place : en absolue, exemple : place(x=50, y=40)
root.mainloop()
