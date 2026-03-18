"""
Contrats de données entre les modules du projet.
Tous les modules doivent respecter ces formats.
"""

from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class FaceDetection:
    x: int          # Coin supérieur gauche
    y: int
    width: int
    height: int
    confidence: float  # Entre 0.0 et 1.0

@dataclass  
class ProcessedFrame:
    original_image: np.ndarray      # Image brute (pour l'affichage)
    preprocessed_image: np.ndarray  # Image prête pour le modèle
    source_id: str                  # "webcam_0" ou "image_chats.jpg"