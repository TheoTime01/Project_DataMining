import json
from random import randint, choice
import os

# Fonction pour charger les caractéristiques d'une image
def load(filename):
    result={}
    with open(filename, "r") as f:
        data=json.load(f)
    #on prend les 577 premiers pokemons (80% du dataset)
    while len(result)<577:
        for i in data:
            result[i]=data[i]
    return result



# Fonction de filtrage en fonction des préférences utilisateur
def filter_images(images, color, legendary):
    filtered_images = []
    img=[]
    for image in images.values():
                if image["color"]["couleur dominante"] == color:
                    tags=image["tags"]["Legendary"]
                    if not(tags^legendary):
                        filtered_images.append(image.get("tags"))
    return filtered_images


# Fonction de génération des préférences utilisateur
def get_user_preferences(images):
    color_t=["rouge","bleu","vert"]
    legendary_t=[True,False]
    color = choice(color_t)
    legendary = choice(legendary_t)
    filtered_images = filter_images(images, color, legendary)
    return filtered_images


#simulation de l'utilisateur
img=load("database.json")
favorite_t=["Favorite","NotFavorite"]
all_user={}

for i in range(500):#100 utilisateurs
    result=[]
    data=get_user_preferences(img)
    for k in range(len(data)):
        result.append(favorite_t[randint(0, len(favorite_t)-1)])
    all_user[i]={'data':data,'result':result}

#sauvegarde des données
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)

