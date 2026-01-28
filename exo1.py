
#TP 1 – R2cupération du nom et de l’âge de l’utilisateur


# 1. Demander le nom et l'âge de l'utilisateur
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

# 2. Afficher s'il est mineur ou majeur
print(f"\nBonjour {nom}!")
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

# 3. Afficher tous les nombres pairs entre 1 et 100
print("\nNombres pairs entre 1 et 100 :")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")

print()  