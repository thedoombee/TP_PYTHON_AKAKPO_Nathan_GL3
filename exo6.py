#TP 6 – Gestion des exceptions 

print("Programme de division \n")

# Boucle pour permettre plusieurs tentatives
continuer = "oui"

while continuer == "oui":
    try:
        # Demander les nombres à l'utilisateur
        numerateur = input("Entrez le numérateur : ")
        denominateur = input("Entrez le dénominateur : ")
        
        # Conversion en nombres
        numerateur = float(numerateur)
        denominateur = float(denominateur)
        
        # Tentative de division
        resultat = numerateur / denominateur
        
        # Affichage du résultat
        print(f"\nRésultat : {numerateur} / {denominateur} = {resultat}")
        
    except ValueError:
        # Gestion des erreurs de saisie invalide
        print("\n Veuillez entrer des nombres valides.")
        print("Exemple : 10, 5.5, -3.2")
        
    except ZeroDivisionError:
        # Gestion de la division par zéro
        print("\n Division par zéro impossible!")
        print("Le dénominateur ne peut pas être égal à zéro.")
        
    except Exception:
        # Gestion des autres erreurs imprévues
        print("\n Une erreur  s'est produite.")
        
    finally:
        # Ce bloc s'exécute toujours
        print("\n" + "-" * 50)
        continuer = input("Voulez-vous faire une autre division? (oui/non) : ")
        print()

