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
    img = []
    out_images = []
    for image in images.values():
            if 'tags' in image:
                for tags in image['tags']:
                    if image["couleur"]["couleur dominante"] == color:
                        if tags.split(":")[0] == 'Legendary':
                            if tags.split(":")[1] == str(legendary):     
                                filtered_images.append(image.get("tags"))
    for item in filtered_images:
        name, type1, type2,generation = "", "", "", ""
        for attr in item:
            key, value = attr.split(":")
            if key == "Name":
                name = value
            elif key == "Type 1":
                type1 = value
            elif key == "Type 2":
                type2 = value
            elif key == "Generation":
                generation = value
        img.append([name, type1, type2, generation]+[color, legendary])
    return img



def get_user_preferences(images):
    color_t=["rouge","bleu","vert"]
    legendary_t=[True,False]
    color = color_t[randint(0, len(color_t)-1)]
    legendary = legendary_t[randint(0, len(legendary_t)-1)]
    filtered_images = filter_images(images, color, legendary)
    return filtered_images


#simulation de l'utilisateur
img=load("database.json")
favorite_t=["Favorite","NotFavorite"]
result=[]
all_user={}

for i in range(100):#100 utilisateurs
    data=get_user_preferences(img)
    for k in range(len(data)):
        result.append(favorite_t[randint(0, len(favorite_t)-1)])
    all_user[i]={'data':data,'result':result}




#sauvegarde des données
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)

