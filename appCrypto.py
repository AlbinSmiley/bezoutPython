import tkinter as tk
from tkinter import ttk
from crypto import crypto

def crypter():
    # Récupérer les valeurs des champs d'entrée
    n = int(entry1.get())
    e = int(entry2.get())
    string = entry3.get()
    
    # Utiliser process_code pour obtenir tous les éléments nécessaires pour l'affichage
    resultat_text = crypto(n,e,string)
    
    # Effacer le contenu précédent et afficher le nouveau résultat
    text_resultat.delete('1.0', tk.END)
    text_resultat.insert('1.0', resultat_text)

def copier_dans_pressepapiers():
    root.clipboard_clear()
    root.clipboard_append(text_resultat.get("1.0", tk.END))

root = tk.Tk()
root.title("Application avec Entrée")
root.geometry("1000x500")  # Ajustez selon les besoins pour une répartition équilibrée

frame_entree = tk.Frame(root)
frame_entree.grid(row=0, column=0, sticky="nsew")

frame_resultat = tk.Frame(root)
frame_resultat.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Champ d'entrée et labels maintenant dans frame_entree
label1 = tk.Label(frame_entree, text="modulo : n =", font=('Arial', 22))
entry1 = tk.Entry(frame_entree, width=10, font=('Arial', 22))
entry1.insert(0, "943")
label1.pack(padx=5, pady=5)
entry1.pack(padx=5, pady=5)

label2 = tk.Label(frame_entree, text="exposant : e =", font=('Arial', 22))
entry2 = tk.Entry(frame_entree, width=10, font=('Arial', 22))
entry2.insert(0, "21")
label2.pack(padx=5, pady=5)
entry2.pack(padx=5, pady=5)

label3 = tk.Label(frame_entree, text="Chaine de caractère à crypter : ", font=('Arial', 22))
entry3 = tk.Entry(frame_entree, width=20, font=('Arial', 22))
entry3.insert(0, "jean est ici")
label3.pack(padx=5, pady=5)
entry3.pack(padx=5, pady=5)

bouton_crypter = tk.Button(frame_entree, text="Crypter", command=crypter, font=('Arial', 22))
bouton_crypter.pack(padx=5, pady=5)

bouton_copier = tk.Button(frame_entree, text="Copier le résultat", command=copier_dans_pressepapiers, font=('Arial', 22))
bouton_copier.pack(padx=5, pady=5)

# Widget Text pour les résultats dans frame_resultat
text_resultat = tk.Text(frame_resultat, height=15, width=50, font=('Arial', 12))
text_resultat.pack(expand=True, fill="both", padx=5, pady=5)

root.mainloop()
