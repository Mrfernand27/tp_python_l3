import csv
import os
from etudiant import Etudiant


class GestionEtudiants:
    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv
        self.etudiants = []
        self.charger()

    def charger(self):
        if not os.path.exists(self.fichier_csv):
            return

        with open(self.fichier_csv, "r", newline="", encoding="utf-8") as f:
            lecteur = csv.DictReader(f)
            for ligne in lecteur:
                nom = ligne["nom"]
                matricule = ligne["matricule"]
                notes_texte = ligne["notes"]

                notes = []
                if notes_texte.strip() != "":
                    parties = notes_texte.split(";")
                    for p in parties:
                        notes.append(float(p))

                self.etudiants.append(Etudiant(nom, matricule, notes))

    def sauvegarder(self):
        with open(self.fichier_csv, "w", newline="", encoding="utf-8") as f:
            champs = ["nom", "matricule", "notes"]
            writer = csv.DictWriter(f, fieldnames=champs)
            writer.writeheader()

            for etu in self.etudiants:
                writer.writerow(etu.to_dict())

    def ajouter_etudiant(self, nom, matricule, notes):
        for e in self.etudiants:
            if e.matricule == matricule:
                print("Erreur : matricule déjà utilisé.")
                return

        self.etudiants.append(Etudiant(nom, matricule, notes))
        self.sauvegarder()
        print("Étudiant ajouté avec succès.")

    def afficher_etudiants(self):
        if len(self.etudiants) == 0:
            print("Aucun étudiant enregistré.")
            return

        print("\n--- LISTE DES ÉTUDIANTS ---")
        for e in self.etudiants:
            print("Nom :", e.nom)
            print("Matricule :", e.matricule)
            print("Notes :", e.notes)
            print("Moyenne :", e.calculer_moyenne())
            print("--------------------------")

    def rechercher_par_matricule(self, matricule):
        for e in self.etudiants:
            if e.matricule == matricule:
                return e
        return None

    def supprimer_etudiant(self, matricule):
        e = self.rechercher_par_matricule(matricule)
        if e is None:
            print("Étudiant introuvable.")
            return

        self.etudiants.remove(e)
        self.sauvegarder()
        print("Étudiant supprimé.")

    def statistiques(self):
        if len(self.etudiants) == 0:
            print("Pas de statistiques : aucun étudiant.")
            return

        somme_moyennes = 0
        for e in self.etudiants:
            somme_moyennes += e.calculer_moyenne()

        moyenne_generale = somme_moyennes / len(self.etudiants)

        meilleur = self.etudiants[0]
        pire = self.etudiants[0]

        for e in self.etudiants:
            if e.calculer_moyenne() > meilleur.calculer_moyenne():
                meilleur = e
            if e.calculer_moyenne() < pire.calculer_moyenne():
                pire = e

        admis = 0
        for e in self.etudiants:
            if e.calculer_moyenne() >= 10:
                admis += 1

        print("\n--- STATISTIQUES ---")
        print("Nombre d'étudiants :", len(self.etudiants))
        print("Moyenne générale :", moyenne_generale)
        print("Admis (>=10) :", admis)
        print("Meilleur :", meilleur.nom, "-", meilleur.calculer_moyenne())
        print("Pire :", pire.nom, "-", pire.calculer_moyenne())
        print("-------------------")
