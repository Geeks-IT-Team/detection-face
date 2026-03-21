import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from preprocess import preprocess

# Cas nominal : image valide
def test_nominal():
    result = preprocess(r"C:\Users\HP\Pictures\Screenshots\hmm.png")
    assert result is not None, "Le résultat ne devrait pas être None"
    assert result.source_id == "hmm.png", "Le source_id ne correspond pas"
    assert result.preprocessed_image.shape == (480, 640, 3), "Les dimensions ne correspondent pas"
    assert result.original_image.shape == (732, 905, 3), "L'image originale ne devrait pas être modifiée"
    print("✅ Test nominal réussi : image valide chargée et prétraitée")

# Cas erreur : fichier inexistant
def test_erreur_fichier_inexistant():
    result = preprocess(r"C:\Users\HP\Pictures\Screenshots\inexistant.png")
    assert result is None, "Le résultat aurait dû être None"
    print("✅ Test erreur réussi : fichier inexistant détecté")

# Cas erreur : fichier corrompu
def test_erreur_fichier_corrompu():
    result = preprocess(r"C:\Users\HP\Desktop\ComputerVisionProject\detection-face\faux.png")
    assert result is None, "Le résultat aurait dû être None"
    print("✅ Test erreur réussi : fichier corrompu détecté")

# Edge case : format non supporté
def test_edge_case_format():
    result = preprocess(r"C:\Users\HP\Pictures\Screenshots\hmm.gif")
    assert result is None, "Le résultat aurait dû être None"
    print("✅ Test edge case réussi : format non supporté détecté")

test_nominal()
test_erreur_fichier_inexistant()
test_erreur_fichier_corrompu()
test_edge_case_format()