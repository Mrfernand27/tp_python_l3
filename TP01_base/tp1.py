# Ajout du nom et du prénom
nom = input("Mettez votre nom: ")
age = int(input("Mettez votre age: "))

# Afficher si majeur ou mineur
if age >= 18:
    print("Vous etes majeur")
else:
    print("Vous etes mineur")

# Afficher les nombres paires entre 1 et 100
for i in range(1,100):
    if i% 2==0:
        print(i)
