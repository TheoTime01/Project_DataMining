import json
from random import randint, choice
import os

# Fonction pour charger les caractéristiques d'une image
def load(filename):
    train={}
    test={}
    with open(filename, "r") as f:
        data=json.load(f)
    for i in data:
        if data[i]["id"]<598:
            train[i]=data[i] #85% des données
        else:
            test[i]=data[i] #15% des données
    return train,test



# Fonction de filtrage en fonction des préférences utilisateur
def filter_images(images, color, legendary):
    filtered_images = []
    for image in images.values():
        if image.get("color", {}).get("couleur dominante") == color:
            tags = image.get("tags", {})
            if bool(tags.get("Legendary")) == bool(legendary):
                image["color"]["couleur dominante"] = color
                filtered_images.append(image)
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
img,test=load("database.json")
favorite_t=["Favorite","NotFavorite"]
all_user={}

for i in range(500):#500 utilisateurs
    result=[]
    data=get_user_preferences(img)
    for k in range(len(data)):
        result.append(favorite_t[randint(0, len(favorite_t)-1)])
    all_user[i]={'data':data,'result':result}

#sauvegarde des données
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)

#sauvegarder les données de test dans un fichier json
with open("test.json", "w") as f:
    json.dump(test, f, indent=4)

