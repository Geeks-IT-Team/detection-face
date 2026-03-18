import cv2
import os

def preprocess(image_path, width=640, height=480):
    """
   La fonction charge et prépare une image pour la détection de visages.
    
    Les arguments:
        image_path: le chemin vers l'image
        width: la largeur de l'image voulue à la sortie
        height: la hauteur de l'image voulue à la sortie
    
    A la sortie : 
        image prétraitée ou message d'erreur s'il y a erreur
    """
    
    # Vérifier le format du fichier
    if not image_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        print(f"Le format de votre image n'est pas supporté, Choisissez une image valide.")
        return None
    
    # Charger l'image
    image = cv2.imread(image_path)
    if image is None:
        if not os.path.exists(image_path):
            print(f"Le fichier '{image_path}' n'existe pas !")
        else:
            print(f"Le fichier '{image_path}' est invalide ou corrompu !")
        return None
    
    # Redimensionner
    image = cv2.resize(image, (width, height))
    
    # Conversion en RGB pour MediaPipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print(f"L'image a bien été chargée avec succès !")
    print(f"Les dimensions de l'image à la sortie : {image.shape}")
    
    return image