import json
from random import randint, choice
import os

# Fonction de filtrage en fonction des préférences utilisateur
def filter_images(images, Type1, Type2, legendary):
    filtered_images = []
    for image in images.values():
        color = image["couleur dominante"]
        type1 = image["tags"]["Type 1"]
        type2 = image["tags"]["Type 2"]
        legendaire = image["tags"]["Legendary"]
        tags= image["tags"]
        if (type1 == Type1 or type2 == Type1) and (type1 == Type2 or type2 == Type2) and not(legendaire^legendary):
            tags["color"]=color
            tags["first_letter"]=tags["Name"][0]
            filtered_images.append(tags)
    return filtered_images

# récuperation des nom couleurs dans database.json
data_t={}
with open("database.json", "r") as f:
    data=json.load(f)
    for i in data:
        data_t[data[i]["id"]]=data[i]

Type_t=[]
for i in data_t:
    if data_t[i]["tags"]["Type 1"] not in Type_t:
        Type_t.append(data_t[i]["tags"]["Type 1"])
    if data_t[i]["tags"]["Type 2"] not in Type_t:
        Type_t.append(data_t[i]["tags"]["Type 2"])

legendary_t=[True, False]

#simulation de l'utilisateur

favorite_t=["favorite","notfavorite"]
all_user={}
nb_user=100
i=0

while i<nb_user:
    result=[]
    Type1=choice(Type_t)
    Type2=choice(Type_t)
    legendary=choice(legendary_t)
    data=filter_images(data_t, Type1, Type2, legendary)
    if len(data)>0:
        for k in range(len(data)):
            result.append(favorite_t[randint(0, len(favorite_t)-1)])
        all_user[i]={"data":data, "result":result}
        i+=1
    else:
        continue

pok=[]
like=[]

for i in all_user:
    for k in range(len(all_user[i]["data"])):
        pok.append(all_user[i]["data"][k])
        like.append(all_user[i]["result"][k])

user={"data":pok, "result":like}


# sauvegarde des données utilisateur
with open("user.json", "w") as f:
    json.dump(user, f, indent=4)




