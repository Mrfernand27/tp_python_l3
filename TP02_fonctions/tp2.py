# Fonction calcul moyenne 
def calcul_moyenne(liste_notes):
    somme=0
    for note in liste_notes:
      somme += note
    moyenne = somme / len(liste_notes)
    return moyenne

# Fonction calcul moyenne
def mention(moyenne):
   if moyenne < 10:
    return "Ajourné"
   elif moyenne < 12:
      return "Passable"
   elif moyenne < 15:
      return "Bien"
   else:
      return "Très bien"
   
# Teste avec une liste de notes
Notes1= [10,15,12]
Notes2= [7,18,9]
Notes3= [13,11,2]
for Notes in [Notes1, Notes2, Notes3]:
   moy= calcul_moyenne(Notes)
   print("Notes: ", Notes)
   print("Moyenne: ", moy)
   print("Mention:", mention(moy))
   print("----------------------------")