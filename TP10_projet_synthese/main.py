from gestion import GestionEtudiants


def demander_notes():
    notes = []
    print("Entrez des notes (tapez 'stop' pour terminer) :")

    while True:
        entree = input("Note : ")

        if entree.lower() == "stop":
            break

        try:
            note = float(entree)
            notes.append(note)
        except ValueError:
            print("Saisie invalide : entrez un nombre ou 'stop'.")

    return notes


def menu():
    print("\n----- MENU -----")
    print("1 - Ajouter un étudiant")
    print("2 - Afficher tous les étudiants")
    print("3 - Rechercher un étudiant (matricule)")
    print("4 - Supprimer un étudiant (matricule)")
    print("5 - Statistiques")
    print("0 - Quitter")
    print("------------------")


def main():
    gestion = GestionEtudiants("etudiants.csv")

    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            nom = input("Nom : ")
            matricule = input("Matricule : ")
            notes = demander_notes()
            gestion.ajouter_etudiant(nom, matricule, notes)

        elif choix == "2":
            gestion.afficher_etudiants()

        elif choix == "3":
            mat = input("Matricule : ")
            e = gestion.rechercher_par_matricule(mat)
            if e is None:
                print("Étudiant introuvable.")
            else:
                print("Nom :", e.nom)
                print("Matricule :", e.matricule)
                print("Notes :", e.notes)
                print("Moyenne :", e.calculer_moyenne())

        elif choix == "4":
            mat = input("Matricule à supprimer : ")
            gestion.supprimer_etudiant(mat)

        elif choix == "5":
            gestion.statistiques()

        elif choix == "0":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")


# IMPORTANT : permet de lancer proprement
if __name__ == "__main__":
    main()
