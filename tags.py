"""ce script permet d'ajouter les tags aux images du dataset"""

import pandas as pd
import json
import csv


df = pd.read_csv(r'C:\Users\Tototime\Desktop\Project_DataMining\data\Pokemon.csv')
df_selected = df.loc[:, ['#','Name', 'Type 1', 'Type 2', 'Total', 'Generation', 'Legendary']]

#change # by id
df_selected.rename(columns={'#': 'id'}, inplace=True)

with open('tags.json', 'w') as f:
    f.write(df_selected.to_json(orient='records')) 

with open('tags.json', 'r') as f:
    data_t = json.load(f)

with open('tags.json', 'w') as f:
    json.dump(data_t, f, indent=4)

with open('database.json', 'r') as f:
    data_d = json.load(f)

# Charger les données de tags.json dans data_d["tags"]
for key in data_d:
    for i in range(len(data_t)):
        if data_d[key]["id"] == data_t[i]["id"]:
            data_d[key]["tags"] = data_t[i]

# Enregistrer les données dans database.json
with open('database.json', 'w') as f:
    json.dump(data_d, f, indent=4)
    