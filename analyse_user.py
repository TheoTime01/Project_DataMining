import json
from random import randint
import os

# Fonction pour charger les caractéristiques d'une image
def load(filename):
    with open(filename, "r") as f:
        return json.load(f)



# Fonction de filtrage en fonction des préférences utilisateur
def filter_images(images, color, legendary):
    filtered_images = []
    for image in images.values():
            if 'tags' in image:
                for tags in image['tags']:
                    if image["couleur"]["couleur dominante"] == color:
                        if tags.split(":")[0] == 'Legendary':
                            if tags.split(":")[1] == str(legendary):     
                                filtered_images.append((image))
    return filtered_images


# Fonction pour demander les préférences utilisateur et filtrer les images en conséquence
def get_user_preferences(images):
    color_t=["rouge","bleu","vert"]
    legendary_t=[True,False]
    color = color_t[randint(0, len(color_t)-1)]
    legendary = legendary_t[randint(0, len(legendary_t)-1)]
    filtered_images = filter_images(images, color, legendary)
    return [filtered_images, color, legendary]


#simulation de l'utilisateur
img=load("database.json")
all_user = {}
for i in range(100):
    user_fav= get_user_preferences(img)

    user= {
        "favorite_color": user_fav[1],
        "legendary": user_fav[2],
        "favorite_pokemons": user_fav[0]
    }

    all_user['id_user'+':'+str(i)] = user
# sauvegarder les préférences utilisateur
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)
