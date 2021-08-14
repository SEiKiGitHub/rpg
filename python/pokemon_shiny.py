import random

oui = ["oui", "Oui", "yes", "Yes", "o", "y"]
non = ["non", "Non", "no", "No", "N", "n"]


def get_shiny(x):
    nb_combat = 0
    nbr_essais = 0
    while True:
        shiny = random.randint(1, x)
        nb_combat += 1
        nbr_essais += 1
        print(f"Combat {nb_combat}..")
        if shiny == 1:
            print("Vous avez trouvé un pokémon shiny au bout de", nbr_essais, "essais !")
            break


reponse = input("Avez vous un charme chroma ?:  ")
if reponse in oui:
    get_shiny(1024)
elif reponse in non:
    get_shiny(2048)