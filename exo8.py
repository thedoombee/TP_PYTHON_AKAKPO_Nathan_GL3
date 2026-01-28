# TP 8 – Algorithmes et Complexité

import time

# 1. Implémenter le tri à bulles
def tri_a_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échanger les éléments
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
    return liste

# 2. Implémenter la recherche linéaire
def recherche_lineaire(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1


# Test du tri à bulles
print("--- Test du tri à bulles ---")
nombres = [64, 34, 25, 12, 22, 11, 90]
print(f"Liste avant tri : {nombres}")
nombres_tries = tri_a_bulles(nombres.copy())
print(f"Liste après tri : {nombres_tries}")

# Test de la recherche linéaire
print("\n--- Test de la recherche linéaire ---")
liste_test = [10, 23, 45, 70, 11, 15]
element_cherche = 70
position = recherche_lineaire(liste_test, element_cherche)
print(f"Liste : {liste_test}")
print(f"Élément recherché : {element_cherche}")
if position != -1:
    print(f"Élément trouvé à la position : {position}")
else:
    print("Élément non trouvé")

# Test avec un élément absent
element_absent = 100
position_absent = recherche_lineaire(liste_test, element_absent)
print(f"\nÉlément recherché : {element_absent}")
if position_absent != -1:
    print(f"Élément trouvé à la position : {position_absent}")
else:
    print("Élément non trouvé")

# 3. Comparer le temps d'exécution avec les fonctions Python
print("\n--- Comparaison des performances ---")

# Créer une grande liste pour les tests
grande_liste = []
for i in range(1000, 0, -1):
    grande_liste.append(i)

# Test du tri à bulles
debut = time.time()
tri_a_bulles(grande_liste.copy())
fin = time.time()
temps_tri_bulles = fin - debut
print(f"Tri à bulles (1000 éléments) : {temps_tri_bulles} secondes")

# Test avec la fonction sorted() de Python
debut = time.time()
sorted(grande_liste.copy())
fin = time.time()
temps_sorted = fin - debut
print(f"Fonction sorted() de Python : {temps_sorted} secondes")

# Comparaison
print(f"\nLa fonction sorted() est environ {temps_tri_bulles / temps_sorted} fois plus rapide")

# Test de recherche linéaire
element_a_trouver = 500
debut = time.time()
recherche_lineaire(grande_liste, element_a_trouver)
fin = time.time()
temps_recherche = fin - debut
print(f"\nRecherche linéaire : {temps_recherche} secondes")

# Comparaison avec 'in' de Python
debut = time.time()
element_a_trouver in grande_liste
fin = time.time()
temps_in = fin - debut
print(f"Opérateur 'in' de Python : {temps_in} secondes")