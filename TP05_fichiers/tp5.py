# Lecture du fichier notes
with open("notes.txt", "r") as fichier:
    notes = fichier.readlines()

# Calcul de la moyenne
somme = 0
for note in notes:
    somme += float(note)
moyenne = somme/ len(notes)
print("La moyenne est: ", moyenne)

# Résultat
with open("resultat.txt", "w") as fichier:
    fichier.write("Moyenne des notes: " + str(moyenne))

