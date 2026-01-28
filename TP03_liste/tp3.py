# Liste de 4 étudiants
etudiants = [
    {"Nom": "ASSIGNON", "Age": 26, "Moyenne": 14 },
    {"Nom": "Fernand", "Age": 20, "Moyenne": 10 },
    {"Nom" : "Komlan", "Age:": 23, "Moyenne": 8 },
    {"Nom":"Orbi", "Age:": 18, "Moyenne": 17 }
]

#Afficher étudiant admis
print("Les étudiants admis sont: ")
for etudiant in etudiants:
    if etudiant["Moyenne"] >= 10:
        print(etudiant["Nom"])

#Calcul moyenne de la classe
somme_moyennes = 0
for etudiant in etudiants:
    somme_moyennes += etudiant["Moyenne"]
moyenne_general = somme_moyennes / len(etudiants)
print("La moyenne de la classe est : ", moyenne_general)