# Importation des bibliothèques nécessaires
import random
import time

def tri_bulles(liste):
    nouvelle_liste = liste.copy()

    # Taille de la liste
    taille = len(nouvelle_liste)
    for i in range(taille):

        # Variable pour vérifier s'il y a eu un échange
        echange = False
        for j in range(0, taille - 1 - i):

            # Comparaison de deux éléments consécutifs
            if nouvelle_liste[j] > nouvelle_liste[j + 1]:
                temp = nouvelle_liste[j]
                nouvelle_liste[j] = nouvelle_liste[j + 1]
                nouvelle_liste[j + 1] = temp
                echange = True

        # Si aucun échange, la liste est déjà triée
        if echange == False:
            break

    return nouvelle_liste

def recherche_lineaire(liste, valeur):
    # On parcourt la liste élément par élément
    for i in range(len(liste)):

        # Si la valeur est trouvée
        if liste[i] == valeur:
            return i  

    # Si la valeur n'est pas trouvée
    return -1

# Taille de la liste
taille_liste = 2000

# Création d'une liste de nombres aléatoires
liste_nombres = []

for i in range(taille_liste):
    nombre = random.randint(0, 100000)
    liste_nombres.append(nombre)

# Choix d'une valeur à rechercher
valeur_recherchee = random.choice(liste_nombres)

print("Taille de la liste :", taille_liste)
print("Valeur à rechercher :", valeur_recherchee)


# Mesure du temps du tri à bulles
debut = time.perf_counter()
liste_triee_bulles = tri_bulles(liste_nombres)
fin = time.perf_counter()

temps_tri_bulles = fin - debut

# Mesure du temps du tri Python 
debut = time.perf_counter()
liste_triee_python = sorted(liste_nombres)
fin = time.perf_counter()

temps_tri_python = fin - debut
print("\n--- COMPARAISON DES TRIS ---")
print("Temps du tri à bulles :", temps_tri_bulles, "secondes")
print("Temps du tri Python (sorted) :", temps_tri_python, "secondes")

# Temps de la recherche linéaire
debut = time.perf_counter()
position_lineaire = recherche_lineaire(liste_nombres, valeur_recherchee)
fin = time.perf_counter()

temps_recherche_lineaire = fin - debut


# Temps de la recherche avec Python
debut = time.perf_counter()
position_python = liste_nombres.index(valeur_recherchee)
fin = time.perf_counter()

temps_recherche_python = fin - debut


print("\n--- COMPARAISON DES RECHERCHES ---")
print("Temps recherche linéaire :", temps_recherche_lineaire, "secondes")
print("Temps recherche Python :", temps_recherche_python, "secondes")
print("Position trouvée (linéaire) :", position_lineaire)
print("Position trouvée (Python) :", position_python)
