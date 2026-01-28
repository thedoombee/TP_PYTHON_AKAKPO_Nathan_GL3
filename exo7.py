#TP 7 – Gestion des étudiants

# 1. Créer une classe Etudiant
class Etudiant:
    # 2. Constructeur avec attributs : nom, matricule, notes
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes
    
    # 3. Méthode pour calculer la moyenne
    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        total = 0
        for note in self.notes:
            total += note
        moyenne = total / len(self.notes)
        return moyenne
    
    # 3. Méthode pour afficher les informations
    def afficher_informations(self):
        print(f"\n{'=' * 50}")
        print(f"Nom : {self.nom}")
        print(f"Matricule : {self.matricule}")
        print(f"Notes : {self.notes}")
        moyenne = self.calculer_moyenne()
        print(f"Moyenne : {moyenne}")
        
        if moyenne >= 10:
            print("Statut : ADMIS")
        else:
            print("Statut : AJOURNÉ")
        print(f"{'=' * 50}")




# Création de plusieurs étudiants
etudiant1 = Etudiant("Kofi MENSAH", "ETU001", [14, 15, 13, 16])
etudiant2 = Etudiant("Ama KODJO", "ETU002", [8, 9, 7, 6])
etudiant3 = Etudiant("Komi AGBEKO", "ETU003", [12, 11, 13, 12])

# Affichage des informations de chaque étudiant
etudiant1.afficher_informations()
etudiant2.afficher_informations()
etudiant3.afficher_informations()

# Utilisation des méthodes
print("\n Calculs de moyennes ")
print(f"{etudiant1.nom} a une moyenne de {etudiant1.calculer_moyenne()}")
print(f"{etudiant2.nom} a une moyenne de {etudiant2.calculer_moyenne()}")
print(f"{etudiant3.nom} a une moyenne de {etudiant3.calculer_moyenne()}")