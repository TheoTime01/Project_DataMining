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
        couleur = image["couleur dominante"]
        legendaire = image["tags"]["Legendary"]
        tags= image["tags"]
        tags["color"]=color # ajouter color dans tags
        # ajouter la lettre du debut du nom du pokemon dans tags
        tags["first_letter"]=tags["Name"][0]
        if couleur == color and not(legendaire^legendary):
            filtered_images.append(tags)
    return filtered_images

# Fonction de génération des préférences utilisateur
def get_user_preferences(images,color_t):
    legendary_t=[True,False]
    color = color_t[randint(0, len(color_t)-1)]
    legendary = legendary_t[randint(0, len(legendary_t)-1)]
    filtered_images = filter_images(images, color, legendary)
    return filtered_images

# récuperation des nom couleurs dans database.json
with open("database.json", "r") as f:
    data=json.load(f)

color_t=[]
for i in data:
    if data[i]["couleur dominante"] not in color_t:
        color_t.append(data[i]["couleur dominante"])


#simulation de l'utilisateur
img,test=load("database.json")

favorite_t=["favorite","notfavorite"]
all_user={}

for i in range(500):#500 utilisateurs
    result=[]
    data=get_user_preferences(img,color_t)
    if len(data)==0:
        continue

    for k in range(len(data)):
        result.append(favorite_t[randint(0, len(favorite_t)-1)])
    all_user[i]={'data':data,'result':result}
    

#sauvegarde des données
with open("user.json", "w") as f:
    json.dump(all_user, f, indent=4)

#sauvegarder les données de test dans un fichier json
with open("test.json", "w") as f:
    json.dump(test, f, indent=4)

