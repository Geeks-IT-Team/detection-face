import cv2
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from interfaces import ProcessedFrame

def preprocess(image_path, width=640, height=480):
    """
    Charge et prépare une image pour la détection de visages.
    
    Args:
        image_path: le chemin complet vers l'image (ex: C:/Users/HP/Pictures/photo.png)
        width: la largeur souhaitée de l'image en sortie (640 pour notre cas)
        height: la hauteur souhaitée de l'image en sortie (480 pour notre cas)
    
    A la sortie :
        ProcessedFrame contenant :
        - l'image brute, originale non modifiée
        - l'image préparée pour le modèle de détection
        - le nom du fichier source
    """
    
    # Vérifier que le fichier est bien une image JPG ou PNG
    if not image_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        print(f"Le format de votre image n'est pas supporté, Choisissez une image valide.")
        return None
    
    # Charger l'image depuis le chemin fourni
    original_image = cv2.imread(image_path)
    if original_image is None:
        if not os.path.exists(image_path):
            print(f"Le fichier '{image_path}' n'existe pas !")
        else:
            print(f"Le fichier '{image_path}' est invalide ou corrompu !")
        return None
    
    # Redimensionner l'image à la taille souhaitée (640 x 480)
    preprocessed_image = cv2.resize(original_image, (width, height))
    
    # Convertir l'image en RGB pour MediaPipe
    preprocessed_image = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2RGB)

    print(f"L'image a bien été chargée avec succès !")
    print(f"Les dimensions de l'image à la sortie : {preprocessed_image.shape}")
    
    return ProcessedFrame(
        original_image=original_image,         # Image brute, d'origine non modifiée
        preprocessed_image=preprocessed_image,  # Image redimensionnée et convertie
        source_id=os.path.basename(image_path)  # Nom du fichier source(cas d'un fichier pour le moment, pour la webcam a gérer plus tard comme convenu)
    )