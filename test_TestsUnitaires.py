from MotDePasse import Generateur # Importation de la fonction Generateur du fichier MotDePasse.py

def test_Peut_Generer_Mot_De_Passe(): # Test de la fonction Generateur.
    
    global Mdp # Déclaration de la variable Mdp en variable globale.
    
    Mdp = Generateur(8, 2) # Appel de la fonction Generateur avec 8 caractères et 2 mots.
    
    assert len(Mdp) == 8 * 2 + (1 * (2/2)) # 8 caractères * 2 mots + 1 tiret.