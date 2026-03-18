from preprocess import preprocess

# Cas nominal : image valide
def test_nominal():
    image = preprocess(r"C:\Users\HP\Pictures\Screenshots\hmm.png")
    assert image is not None, "L'image ne devrait pas être None"
    print("Test nominal réussi : image valide chargée et prétraitée")

# Cas erreur : fichier inexistant
def test_erreur_fichier_inexistant():
    image = preprocess(r"C:\Users\HP\Pictures\Screenshots\inexistant.png")
    assert image is None, "La fonction aurait dû retourner None"
    print("Test erreur réussi : fichier inexistant détecté")

# Cas erreur : fichier corrompu
def test_erreur_fichier_corrompu():
    image = preprocess(r"C:\Users\HP\Desktop\ComputerVisionProject\detection-face\faux.png")
    assert image is None, "La fonction aurait dû retourner None"
    print("Test erreur réussi : fichier corrompu détecté")

# Edge case : format non supporté
def test_edge_case_format():
    image = preprocess(r"C:\Users\HP\Pictures\Screenshots\hmm.gif")
    assert image is None, "La fonction aurait dû retourner None"
    print("Test edge case réussi : format non supporté détecté")

test_nominal()
test_erreur_fichier_inexistant()
test_erreur_fichier_corrompu()
test_edge_case_format()