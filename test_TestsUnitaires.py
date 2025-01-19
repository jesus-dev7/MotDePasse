from MotDePasse import Generateur # Importation de la fonction Generateur du fichier MotDePasse.py

from MotDePasse import TestForce

def test_Peut_Generer_Mot_De_Passe(): # Test de la fonction Generateur.
    
    global Mdp # Déclaration de la variable Mdp en variable globale.
    
    Mdp = Generateur(8, 3) # Appel de la fonction Generateur avec 8 caractères et 3 mots.
    
    assert len(Mdp) == 8 * 3 + 3 - 1 # 8 caractères * 3 mots + 3 tirets - 1 tiret.
    
def test_Renvoie_Une_Force():
    
    global Mdp
    
    Force = TestForce(Mdp)
    
    assert type(Force) == float