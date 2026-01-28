# Demande de la phrase
phrase = input("Mettez une phrase: ")

#Compter le nombre de mots
mots= phrase.split()
nb_mots = len(mots)
print("Le nombre de mot est: ", nb_mots)

#Mot le plus long
mot_plus_long= mots[0]
for mot in mots:
    if len(mot) > len(mot_plus_long):
        mot_plus_long=mot
        print("Le mot le plus long est: ", mot_plus_long)

# Vérifier le palindrome
phrase_sans_espace = phrase.replace(" ", "")
phrase_nettoyee = phrase_sans_espace.lower()
inverse = phrase_nettoyee[::-1]
if phrase_nettoyee ==inverse:
    print("La phrase est un palindrome")
else:
    print("La phrase n'est pas un palindrome")