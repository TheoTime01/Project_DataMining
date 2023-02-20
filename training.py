""" this script is used to train the model """
import os
import json
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plot
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# specify the path to the JSON file
json_path = r"C:\Users\Tototime\Desktop\Project_DataMining\database.json"


# load the data
with open(json_path, 'r') as f:
    data = json.load(f)
    X = []
    Y = []
    for image in data.values():
        # get the features
        features = []
        for tag in image['tags']:
            features.append(tag.split(":")[1])
        X.append(features)
        # get the target
        color = image['couleur']['couleur dominante']
        if color == "rouge":
            y.append(0)
        elif color == "vert":
            y.append(1)
        else:
            y.append(2)

# convert the data to numpy arrays
x = np.array(X)
y = np.array(Y)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# scale the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# train the model
mlp = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=1000)
mlp.fit(X_train, y_train)

# make predictions
predictions = mlp.predict(X_test)

# evaluate the model
print("Accuracy:", metrics.accuracy_score(y_test, predictions))
print("Precision:", metrics.precision_score(y_test, predictions, average='macro'))
print("Recall:", metrics.recall_score(y_test, predictions, average='macro'))
print("F1:", metrics.f1_score(y_test, predictions, average='macro'))

# plot the confusion matrix
cm = confusion_matrix(y_test, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["rouge", "vert", "bleu"])
disp.plot()
plot.show()




