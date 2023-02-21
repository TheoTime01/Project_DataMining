import json
from random import randint
import os

# Fonction pour charger les caractéristiques d'une image
def load(filename):
    result={}
    with open(filename, "r") as f:
        data=json.load(f)
    #on prend les 577 premiers pokemons
    while len(result)<577:
        for i in data:
            result[i]=data[i]
    return result



# Fonction de filtrage en fonction des préférences utilisateur
def filter_images(images, color, legendary):
    filtered_images = []
    for image in images.values(): #on prend les 577 premiers pokemons
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
    like=randint(0,1) # 0 pour dislike et 1 pour like
    filtered_images = filter_images(images, color, legendary)
    return [filtered_images, color, legendary,like]


#simulation de l'utilisateur
img=load("database.json")
all_user = {}
for i in range(100):
    user_fav= get_user_preferences(img)

    user= {
        "like": user_fav[3],
        "color": user_fav[1],
        "legendary": user_fav[2],
        "pokemons": user_fav[0],
    }

    all_user['id_user'+':'+str(i)] = user
# sauvegarder les préférences utilisateur
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)
