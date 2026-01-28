# Travaux Pratiques Python - Licence 3
# AKAKPO Nathan GL_3
## Enseignant : Ing GBADAMASSI ABDOU-AKIM

---

## Description du Repository

Ce repository contient l'ensemble des travaux pratiques (TP) du module Python de niveau Licence 3, réalisés le **Mercredi 28 janvier 2026**.

L'objectif de ces TP est de développer une logique de programmation solide et d'acquérir les compétences nécessaires pour devenir un bon informaticien ou technicien dans le domaine technologique.

---

## Liste des Travaux Pratiques

### TP 1 – Prise en main et structures de base
**Fichier :** `tp1_structures_base.py`

**Contexte :** Création d'un premier script utilisé par un service de scolarité

**Compétences :**
- Variables et input/output
- Structures conditionnelles (if/else)
- Boucles (for)

**Fonctionnalités :**
1. Demande le nom et l'âge de l'utilisateur
2. Affiche si l'utilisateur est mineur ou majeur
3. Affiche tous les nombres pairs entre 1 et 100

---

### TP 2 – Fonctions et modularité
**Fichier :** `tp2_fonctions.py`

**Contexte :** Automatisation du calcul des moyennes d'une classe

**Compétences :**
- Définition de fonctions (def)
- Paramètres et valeurs de retour

**Fonctionnalités :**
1. Fonction `calcul_moyenne()` pour calculer la moyenne d'une liste de notes
2. Fonction `mention()` pour déterminer la mention (Ajourné, Passable, Bien, Très bien)
3. Tests avec plusieurs listes de notes

---

### TP 3 – Listes, tuples et dictionnaires
**Fichier :** `tp3_listes_dicts.py`

**Contexte :** Gestion simplifiée des résultats académiques

**Compétences :**
- Listes et dictionnaires
- Parcours de collections

**Fonctionnalités :**
1. Stockage d'une liste d'étudiants (nom, âge, moyenne)
2. Affichage des étudiants admis (moyenne ≥ 10)
3. Calcul de la moyenne générale de la classe

---

### TP 4 – Manipulation de chaînes de caractères
**Fichier :** `tp4_chaines.py`

**Contexte :** Analyse de commentaires saisis par des utilisateurs

**Compétences :**
- Méthodes sur les chaînes
- Découpage et analyse de texte

**Fonctionnalités :**
1. Demande une phrase à l'utilisateur
2. Compte le nombre de mots
3. Trouve le mot le plus long
4. Vérifie si la phrase est un palindrome

---

### TP 5 – Fichiers (lecture et écriture)
**Fichier :** `tp5_fichiers.py`

**Contexte :** Sauvegarde et exploitation de données scolaires

**Compétences :**
- Fonction open()
- Modes de fichiers (r, w, a)

**Fonctionnalités :**
1. Crée un fichier `notes.txt` contenant des notes
2. Lit le fichier et calcule la moyenne
3. Écrit le résultat dans `resultat.txt`

**Fichiers générés :**
- `notes.txt` : Fichier contenant les notes
- `resultat.txt` : Fichier contenant les résultats

---

### TP 6 – Gestion des exceptions
**Fichier :** `tp6_exceptions.py`

**Contexte :** Sécurisation d'une application utilisée par des non-informaticiens

**Compétences :**
- try / except / finally
- Gestion des erreurs

**Fonctionnalités :**
1. Programme de division sécurisé
2. Gestion de la division par zéro
3. Gestion des saisies invalides
4. Messages d'erreur personnalisés

---

### TP 7 – Programmation Orientée Objet (POO)
**Fichier :** `tp7_poo.py`

**Contexte :** Modélisation d'un système de gestion des étudiants

**Compétences :**
- Création de classes (class)
- Constructeur (__init__)
- Méthodes d'instance

**Fonctionnalités :**
1. Classe `Etudiant` avec attributs (nom, matricule, notes)
2. Méthode `calculer_moyenne()`
3. Méthode `afficher_informations()`

---

### TP 8 – Algorithmes et complexité
**Fichier :** `tp8_algorithmes.py`

**Contexte :** Optimisation d'un programme utilisé à grande échelle

**Compétences :**
- Implémentation d'algorithmes
- Analyse de complexité
- Mesure de performances

**Fonctionnalités :**
1. Implémentation du tri à bulles
2. Implémentation de la recherche linéaire
3. Comparaison des performances avec les fonctions Python natives

---

### TP 9 – Manipulation de données (CSV)
**Fichier :** `tp9_csv.py`

**Contexte :** Analyse de données RH d'une entreprise

**Compétences :**
- Module csv
- Structuration des données
- Génération de rapports

**Fonctionnalités :**
1. Lecture d'un fichier CSV d'employés
2. Calcul du salaire moyen par département
3. Génération d'un rapport textuel

**Fichiers générés :**
- `employes.csv` : Base de données des employés
- `rapport_rh.txt` : Rapport d'analyse

---

### TP 10 – Mini-projet de synthèse
**Fichier :** `tp10_mini_projet.py`

**Contexte :** Développement d'une application complète de gestion

**Compétences :**
- Intégration de tous les concepts
- POO
- Fichiers
- Statistiques
- Interface utilisateur en console

**Fonctionnalités :**
1. Gestion complète des étudiants (ajout, affichage)
2. Sauvegarde et chargement des données depuis CSV
3. Calcul et affichage de statistiques détaillées
4. Interface menu interactive

**Classes :**
- `Etudiant` : Représente un étudiant
- `GestionEtudiants` : Gère la collection d'étudiants

---

## Installation et Utilisation

### Prérequis
- Python 3.x installé sur votre machine

### Exécution des TP

Pour exécuter un TP, utilisez la commande suivante dans votre terminal :

```bash
python tp1_structures_base.py
```

Remplacez `tp1_structures_base.py` par le nom du fichier que vous souhaitez exécuter.

### Ordre recommandé
Il est conseillé de suivre les TP dans l'ordre (TP1 à TP10) car ils progressent en complexité et chaque TP s'appuie sur les concepts des TP précédents.

---

## Notes importantes

### Niveau de compétences
Chaque TP est conçu pour utiliser **uniquement** les compétences mentionnées dans les objectifs. Aucune fonctionnalité avancée non enseignée n'a été utilisée.

### Structure du code
- Code simple et lisible
- Commentaires explicatifs
- Respect des bonnes pratiques Python
- Variables en français pour correspondre au contexte académique

### Fichiers générés
Certains TP créent des fichiers de données :
- TP5 : `notes.txt`, `resultat.txt`
- TP9 : `employes.csv`, `rapport_rh.txt`
- TP10 : Fichiers CSV personnalisés selon vos sauvegardes

---

## Conseils pour les étudiants

> "Il faut travailler avec sagesse et vous êtes les responsables de votre vie, tu es bien avec de bonnes attitudes et l'humilité en informatique tu auras de bonnes places !!!!"

> "Tu veux être convoité fait plus que moi, ce n'est pas facile mais avec de la pratique ça ira"

### Pour réussir vos TP :
1. **Lisez attentivement** les commentaires dans le code
2. **Testez** chaque programme plusieurs fois avec différentes entrées
3. **Modifiez** le code pour comprendre ce que fait chaque partie
4. **Expérimentez** : ajoutez vos propres fonctionnalités
5. **Pratiquez régulièrement** : la programmation s'apprend par la pratique

---

## Contact

**Enseignant :** Ing GBADAMASSI ABDOU-AKIM  
**Email :** gbadamassia@gmail.com | developpe@fit-entreprise.com  
**Fonction :** Senior Software Engineer | Consultant informatique CCI TOGO  
**Site :** https://ingenieur-gbadamassi.com

---

##  Date de réalisation
Mercredi 28 janvier 2026 - À rendre avant 18H50

---

##  Objectif pédagogique

Ce TP est conçu pour vous mettre sur les rails et développer une logique de programmation très poussée. L'objectif est de vous faire réfléchir comme un bon informaticien ou technicien dans le domaine technologique pour vos projets futurs liés à Python.

Ces exercices ont été pensés pour vous faire gravir les échelons après ce module Python.

---

**Bon courage et bonne programmation ! 🚀**
