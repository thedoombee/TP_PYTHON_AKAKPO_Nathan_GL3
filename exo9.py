"""
TP 9 – Manipulation de données (CSV)
Contexte : Analyse de données RH d'une entreprise
Compétences : module csv, structuration des données
"""

import csv

# 1. Créer un fichier CSV d'employés pour les tests
print("=== Création du fichier CSV employés ===")
fichier = open("employes.csv", "w")
fichier.write("nom,prenom,departement,salaire\n")
fichier.write("MENSAH,Kofi,Informatique,450000\n")
fichier.write("KODJO,Ama,Informatique,500000\n")
fichier.write("AGBEKO,Kwame,RH,380000\n")
fichier.write("ABBEY,Efua,RH,420000\n")
fichier.write("TETTEH,Koffi,Finance,550000\n")
fichier.write("KOMLAN,Adjoa,Finance,520000\n")
fichier.write("DOE,Edem,Informatique,480000\n")
fichier.write("AHONTO,Sena,RH,400000\n")
fichier.close()
print("Fichier employes.csv créé avec succès.\n")

# 1. Lire le fichier CSV d'employés
print("=== Lecture du fichier CSV ===")
fichier = open("employes.csv", "r")
lecteur = csv.DictReader(fichier)

employes = []
for ligne in lecteur:
    employe = {
        "nom": ligne["nom"],
        "prenom": ligne["prenom"],
        "departement": ligne["departement"],
        "salaire": float(ligne["salaire"])
    }
    employes.append(employe)

fichier.close()

print(f"Nombre d'employés lus : {len(employes)}\n")

# 2. Calculer le salaire moyen par département
print("=== Calcul du salaire moyen par département ===")

# Créer un dictionnaire pour stocker les salaires par département
departements = {}

for employe in employes:
    dept = employe["departement"]
    salaire = employe["salaire"]
    
    if dept not in departements:
        departements[dept] = []
    
    departements[dept].append(salaire)

# Calculer les moyennes
moyennes_departements = {}
for dept in departements:
    total = 0
    for salaire in departements[dept]:
        total += salaire
    moyenne = total / len(departements[dept])
    moyennes_departements[dept] = moyenne

# Afficher les résultats
for dept in moyennes_departements:
    print(f"{dept} : {moyennes_departements[dept]} FCFA")

# 3. Générer un rapport textuel
print("\n=== Génération du rapport ===")
fichier = open("rapport_rh.txt", "w")

fichier.write("=" * 60 + "\n")
fichier.write("RAPPORT D'ANALYSE DES SALAIRES PAR DÉPARTEMENT\n")
fichier.write("=" * 60 + "\n\n")

fichier.write(f"Total des employés : {len(employes)}\n\n")

fichier.write("SALAIRE MOYEN PAR DÉPARTEMENT\n")
fichier.write("-" * 60 + "\n")

for dept in moyennes_departements:
    nombre_employes = len(departements[dept])
    moyenne = moyennes_departements[dept]
    fichier.write(f"\n{dept} :\n")
    fichier.write(f"  - Nombre d'employés : {nombre_employes}\n")
    fichier.write(f"  - Salaire moyen : {moyenne} FCFA\n")

fichier.write("\n" + "=" * 60 + "\n")
fichier.write("LISTE DÉTAILLÉE DES EMPLOYÉS\n")
fichier.write("=" * 60 + "\n\n")

for employe in employes:
    fichier.write(f"{employe['prenom']} {employe['nom']} - ")
    fichier.write(f"{employe['departement']} - ")
    fichier.write(f"{employe['salaire']} FCFA\n")

fichier.close()
print("Rapport généré dans rapport_rh.txt\n")

# Afficher le rapport
print("=== Contenu du rapport ===")
fichier = open("rapport_rh.txt", "r")
for ligne in fichier:
    print(ligne, end="")
fichier.close()