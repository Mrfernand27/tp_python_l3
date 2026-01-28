# Importation du module csv
import csv

# Dictionnaire pour stocker les salaires par département
salaires_par_departement = {}

# LECTURE DU FICHIER CSV
with open("employes.csv", "r", newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)

    # Parcours de chaque ligne du fichier CSV
    for ligne in lecteur:
        departement = ligne["departement"]
        salaire = float(ligne["salaire"])

        # Si le département n'existe pas encore dans le dictionnaire
        if departement not in salaires_par_departement:
            salaires_par_departement[departement] = []

        # Ajouter le salaire dans la liste du département
        salaires_par_departement[departement].append(salaire)

# CALCUL DU SALAIRE MOYEN PAR DÉPARTEMENT
moyennes = {}

for departement in salaires_par_departement:
    liste_salaires = salaires_par_departement[departement]

    somme = 0
    for salaire in liste_salaires:
        somme += salaire

    moyenne = somme / len(liste_salaires)

    moyennes[departement] = moyenne

# RAPPORT
with open("rapport.txt", "w", encoding="utf-8") as fichier:
    fichier.write("RAPPORT DES SALAIRES PAR DÉPARTEMENT\n")
    fichier.write("----------------------------------\n")

    for departement in moyennes:
        fichier.write(
            "Département : " + departement +
            " | Salaire moyen : " + str(moyennes[departement]) + "\n"
        )

print("Rapport généré avec succès.")
