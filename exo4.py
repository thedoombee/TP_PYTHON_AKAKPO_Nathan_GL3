#TP 4 – Analyse d'une phrase

# 1. Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase : ")

# 2. Compter le nombre de mots
# donc ici on divise la phrase en utilisants l'espace comme séparateur et on mstock ça dans mots 
mots = phrase.split()
nombre_mots = len(mots)
print(f"\nNombre de mots : {nombre_mots}")

# 3. Trouver le mot le plus long
mot_plus_long = ""
for mot in mots:
    if len(mot) > len(mot_plus_long):
        mot_plus_long = mot

print(f"Mot le plus long : {mot_plus_long} ({len(mot_plus_long)} caractères)")

# 4. Vérifier si la phrase est un palindrome
# Retirer les espaces et mettre en minuscules pour la comparaison
phrase_sans_espaces = phrase.replace(" ", "").lower()
phrase_inversee = ""

# Inverser la phrase
for caractere in phrase_sans_espaces:
    phrase_inversee = caractere + phrase_inversee

# Vérifier si c'est un palindrome
if phrase_sans_espaces == phrase_inversee:
    print(f"La phrase '{phrase}' est un palindrome.")
else:
    print(f"La phrase '{phrase}' n'est pas un palindrome.")