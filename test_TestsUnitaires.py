from MotDePasse import Generateur

def test_Peut_Generer_Mot_De_Passe():
    
    global Mdp
    
    Mdp = Generateur(8, 2)
    
    assert len(Mdp) == 8 * 2 + (1 * (2/2))