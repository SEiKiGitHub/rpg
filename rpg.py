import random

ennemy_hp, player_hp = 50, 50
potion = 3
skip_turn = False
nb_tour = 1

while True:
    print(f"Tour {nb_tour}")
    if skip_turn:
        print("vous passez votre tour")
        skip_turn = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            print("Attaquer: 1 | Potion: 2")
            user_choice = input("> ")

            if user_choice == "1":
                dmg = random.randint(5, 10)
                ennemy_hp -= dmg
                print("Vous avez enlevé", dmg, "a votre adversaire!")
            elif user_choice == "2":
                if potion > 0:
                    pv = random.randint(15, 50)
                    potion -= 1
                    player_hp += pv
                    print("Vous avez utilisé une potion qui vous a rajouté", pv, "pv!")
                    skip_turn = True
                else:
                    print("Vous n'avez plus de potions")
                    continue
    if ennemy_hp < 0:
        print("Vous avez gagné")
        break

    ennemy_dmg = random.randint(5, 15)
    player_hp -= ennemy_dmg
    print("Vous avez perdu", ennemy_dmg, "pv!")
    if player_hp < 0:
        print("Vous avez perdu")
        break

    print("Il vous reste", player_hp, "pv")
    print("Il reste a votre adversaire", ennemy_hp, "pv")
    nb_tour += 1
    print("-"*50)

print(f"La partie s'est fini en {nb_tour} tours")
