import random

lettre_cachee = chr(random.randint(65, 90))  # Génère une lettre aléatoire entre 'A' et 'Z'

lettres_trouvees = []
nb_lettres_trouvees = 0

nb_tentatives = 0
max_tentatives = 10

print("Bienvenue dans le jeu de recherche de lettre !")

while nb_tentatives < max_tentatives:
    lettre = input("Veuillez entrer une lettre : ")

    if lettre in lettres_trouvees:
        print("Vous avez déjà trouvé cette lettre !")
        continue

    nb_tentatives += 1

    if lettre == lettre_cachee:
        print(f"Félicitations ! Vous avez trouvé la lettre cachée ({lettre}) en {nb_tentatives} tentative(s) !")
        break
    else:
        print("Dommage ! La lettre que vous avez entrée n'est pas la bonne.")

        if lettre < lettre_cachee:
            print("La lettre recherchée est plus grande.")
        else:
            print("La lettre recherchée est plus petite.")

    lettres_trouvees.append(lettre)
    nb_lettres_trouvees += 1

    if nb_tentatives == max_tentatives:
        print(f"Vous avez épuisé toutes vos tentatives. La lettre cachée était : {lettre_cachee}")
