#TP 5 – Gestion de fichiers et calcul de moyenne

# 1. Créer un fichier notes.txt contenant des notes
fichier = open("notes.txt", "w")
fichier.write("15\n")
fichier.write("12\n")
fichier.write("14\n")
fichier.write("16\n")
fichier.write("11\n")
fichier.write("13\n")
fichier.close()

print("Fichier notes.txt créé avec succès.")

# 2. Lire le fichier et calculer la moyenne
fichier = open("notes.txt", "r")
notes = []
for ligne in fichier:
    note = float(ligne)
    notes.append(note)
fichier.close()

total = 0
for note in notes:
    total += note

moyenne = total / len(notes)

print(f"\nNotes lues : {notes}")
print(f"Moyenne calculée : {moyenne}")

# 3. Écrire le résultat dans un fichier resultat.txt
fichier = open("resultat.txt", "w")
fichier.write(" Résultats \n")
fichier.write(f"Nombre de notes : {len(notes)}\n")
fichier.write(f"Notes : {notes}\n")
fichier.write(f"Moyenne : {moyenne}\n")

if moyenne >= 10:
    fichier.write("Résultat : ADMIS\n")
else:
    fichier.write("Résultat : AJOURNÉ\n")

fichier.close()

print("\nRésultat écrit dans resultat.txt")

# Afficher le contenu du fichier resultat.txt
fichier = open("resultat.txt", "r")
for ligne in fichier:
    print(ligne, end="")
fichier.close()