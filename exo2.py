#TP 2 – Calcul de la moyenne et détermination de la mention

# 1. Fonction pour calculer la moyenne
def calcul_moyenne(liste_notes):
    if len(liste_notes) == 0:
        return 0
    total = 0
    for note in liste_notes:
        total += note
    moyenne = total / len(liste_notes)
    return moyenne

# 2. Fonction pour déterminer la mention
def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Bien"
    else:
        return "Très bien"

# 3. Tests avec plusieurs listes de notes
print(" Les listes de notes à tester\n")

# Test 1
notes_etudiant1 = [12, 14, 13, 15]
moyenne1 = calcul_moyenne(notes_etudiant1)
print(f"Étudiant 1 - Notes : {notes_etudiant1}")
print(f"Moyenne : {moyenne1}")
print(f"Mention : {mention(moyenne1)}\n")

# Test 2
notes_etudiant2 = [8, 9, 7, 6]
moyenne2 = calcul_moyenne(notes_etudiant2)
print(f"Étudiant 2 - Notes : {notes_etudiant2}")
print(f"Moyenne : {moyenne2}")
print(f"Mention : {mention(moyenne2)}\n")

# Test 3
notes_etudiant3 = [16, 17, 18, 15]
moyenne3 = calcul_moyenne(notes_etudiant3)
print(f"Étudiant 3 - Notes : {notes_etudiant3}")
print(f"Moyenne : {moyenne3}")
print(f"Mention : {mention(moyenne3)}\n")

# Test 4
notes_etudiant4 = [10, 11, 12, 10]
moyenne4 = calcul_moyenne(notes_etudiant4)
print(f"Étudiant 4 - Notes : {notes_etudiant4}")
print(f"Moyenne : {moyenne4}")
print(f"Mention : {mention(moyenne4)}")