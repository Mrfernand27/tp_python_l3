# Classe etudiant
# Classe Etudiant
class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

# Calcul de moyenne
    def calculer_moyenne(self):
     somme = 0
     for note in self.notes:
       somme += note
     moyenne = somme / len(self.notes)
     return moyenne

    # Afficher les informations
    def afficher_informations(self):
        print("Nom :", self.nom)
        print("Matricule :", self.matricule)
        print("Notes :", self.notes)
        print("Moyenne :", self.calculer_moyenne())

# ----- Programme principal -----
etudiant1 = Etudiant(
    "ASSIGNON Fernand",
    "ETU001",
    [12, 13, 10, 10]
)

etudiant1.afficher_informations()    