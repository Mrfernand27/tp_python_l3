class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0

        somme = 0
        for note in self.notes:
            somme += note

        moyenne = somme / len(self.notes)
        return moyenne

    def to_dict(self):
        # notes => "12;15;10"
        notes_str = ""
        for i in range(len(self.notes)):
            notes_str += str(self.notes[i])
            if i < len(self.notes) - 1:
                notes_str += ";"

        return {
            "nom": self.nom,
            "matricule": self.matricule,
            "notes": notes_str
        }
