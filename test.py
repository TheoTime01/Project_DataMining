def tag_image(img_path):
    # Extract features from the image
    features = extract_features(img_path)

    # Use the trained model to predict the tags
    tags = clf.predict([features])[0]
    return tags


def get_main_color(image):
    # Vérifier que l'image existe
    if not os.path.isfile(image):
        print(f"Le fichier {image} n'existe pas")
        return

    # Ouvrir l'image
    with Image.open(image) as img:
        # Extraire la matrice de pixels
        pixel_matrix = np.array(img)

        # Extraire les valeurs R, G, B
        r = pixel_matrix[:, :, 0].flatten()
        g = pixel_matrix[:, :, 1].flatten()
        b = pixel_matrix[:, :, 2].flatten()

        # Calculer la couleur moyenne
        mean_r = np.mean(r)
        mean_g = np.mean(g)
        mean_b = np.mean(b)

        # Déterminer la couleur prédominante
        if mean_r >= mean_g and mean_r >= mean_b:
            main_color = "rouge"
        elif mean_g >= mean_r and mean_g >= mean_b:
            main_color = "vert"
        else:
            main_color = "bleu"

        # Retourner la couleur prédominante et les valeurs moyennes
        return {
            "couleur_predominante": main_color,
            "valeur_moyenne_rouge": str(mean_r),
            "valeur_moyenne_vert": str(mean_g),
            "valeur_moyenne_bleu": str(mean_b),
        }

# Exemple d'utilisation de la fonction
image_file = Images[int(num_image) - 1]
details = get_main_color(image_file)

if details is not None:
    print(f"La couleur prédominante de l'image est {details['couleur_predominante']}")
    print(f"Valeur moyenne rouge: {details['valeur_moyenne_rouge']}")
    print(f"Valeur moyenne vert: {details['valeur_moyenne_vert']}")
    print(f"Valeur moyenne bleu: {details['valeur_moyenne_bleu']}")

    # Écrire les détails dans un fichier JSON
    with open("Fichier.json", "a") as json_file:
        json.dump(details, json_file)
        json_file.write("\n") # ajouter une nouvelle ligne pour chaque entrée