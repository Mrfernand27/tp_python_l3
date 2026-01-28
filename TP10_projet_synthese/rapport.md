# TP10 – Mini-projet de synthèse : Gestion des étudiants

## Objectif
Développer une application Python permettant :
- gérer des étudiants (ajout, affichage, recherche, suppression)
- enregistrer les données dans un fichier CSV
- afficher des statistiques
- utiliser la programmation orientée objet (POO)

## Organisation des fichiers
- `etudiant.py` : classe `Etudiant` (nom, matricule, notes + moyenne)
- `gestion.py` : classe `GestionEtudiants` (chargement, sauvegarde, stats)
- `main.py` : menu utilisateur + exécution du programme
- `etudiants.csv` : fichier de persistance des données

## Stockage des données
Le fichier `etudiants.csv` contient :
- nom
- matricule
- notes (stockées sous forme : `12;15;10`)

## Statistiques
- nombre d'étudiants
- moyenne générale
- nombre d'admis (moyenne >= 10)
- meilleur étudiant
- pire étudiant

## Exécution
Dans le dossier du projet :
`bash
python main.py
