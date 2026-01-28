#TP 3 – Gestion d'une liste d'étudiants et calcul de la moyenne générale

# 1. Stocker une liste d'étudiants (nom, âge, moyenne)
etudiants = [
    {"nom": "Kofi", "age": 20, "moyenne": 14.5},
    {"nom": "Ama", "age": 19, "moyenne": 9.5},
    {"nom": "Kodjo", "age": 21, "moyenne": 12.0},
    {"nom": "Afi", "age": 20, "moyenne": 16.0},
    {"nom": "Komi", "age": 22, "moyenne": 8.0},
    {"nom": "Adjoa", "age": 19, "moyenne": 11.5}
]

print("Liste des étudiants")
for etudiant in etudiants:
    print(f"Nom: {etudiant['nom']}, Âge: {etudiant['age']}, Moyenne: {etudiant['moyenne']}")

# 2. Afficher les étudiants admis (moyenne >= 10)
print("\n=== Étudiants admis (moyenne >= 10) ===")
for etudiant in etudiants:
    if etudiant["moyenne"] >= 10:
        print(f"{etudiant['nom']} - Moyenne: {etudiant['moyenne']}")

# 3. Calculer la moyenne générale de la classe
total_moyennes = 0
for etudiant in etudiants:
    total_moyennes += etudiant["moyenne"]

moyenne_generale = total_moyennes / len(etudiants)
print(f"Moyenne générale des étudiants: {moyenne_generale:.2f}")