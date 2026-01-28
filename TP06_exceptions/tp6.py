# Demande des valeurs a l'utilisateurs
try:
    a = float(input("Entrer le 1er nombre: "))
    b = float(input("Entrer le 2ièm nombre: "))
    resultat = a/b
    print("Le résultat de la division est: ", resultat)
except ZeroDivisionError:
    print("Erreur: division par 0 impossible.")
except ValueError:
    print("Erreur: veuillez entrer uniquement des nombres")
finally:
    print("Fin du programme")