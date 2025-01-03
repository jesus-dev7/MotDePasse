#imports
import string
import random
from collections import Counter
from string import punctuation
import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import ttk, messagebox
from tkinter import Tk, Label
from PIL import Image, ImageTk

#Definition variables
alphabet = string.ascii_lowercase #Les caractères en minuscule.
ChoixUser = 0
NombreDeMots = 0
ListePremiereLettre = []
MotSuivant = 0
set(punctuation) #Liste des caractères spéciaux.
chiffres = "0123456789" #Définition des chiffres sous forme d'une chaîne de caractères.
set(chiffres) #Liste des chiffres.



#tkinter
def tkinter():
    """Fenêtre tkinter pour le test de force

    E: type: None, None
    
    S: type: None, None
    """
    
    global CompteurE #On peut l'utiliser dans d'autres fonctions.
    CompteurE = 0 #Définir la variable.
    
    #Vérification systématique de la saisie utilisateur
    def validation(text):
        """Fonction de vérification permanente de saisie utilisateur.

        Args:
            text (_str_): Le mot de passe.

        Returns:
            Bool: Si on permet d'écrire.
        """
        
        global CompteurE #On fait référence à une variable définie en dehors de la fonction ce qui nous permet de la modifiée même si elle n'est pas définie dans la fonction.
        
        
        if len(text) >= 7 and any(text[i:i+7].islower() and text[i:i+7].isalpha() for i in range(len(text) - 6)) or len(text) >= 4 and any(text[i:i+4].isdigit() for i in range(len(text) - 3)): #On regarde si le texte fait un certain nombre de caractères et si dans les sous-chaînes créées à partir de la chaîne de caractère qu'est le mot de passe il y a des caractères qui s'enchaînent trop. On ne traite pas les sous-chaînes qui ne sont pas complètes.
            
            messagebox.showerror("Erreur", "Pour avoir un mot de passe sécurisé, veuillez s'il vous plait, varier les caractères.") #popup erreur
            
            CompteurE += 1 #On compte le nombre d'erreurs affichées.
            
            if CompteurE == 3: #Si le nombre d'erreurs est de trois.
                
                TroisErreurs() #Appelle la fonction.
                
                CompteurE = 0 #On remet le compteur à zéro pour que l'utilisateur puisse écrire à nouveau.
                
            return False #On empêche d'écrire.
        
        return True #Retourne True.


    def TroisErreurs():
        """Fonction qui affcihe une erreur et qui efface l'entrée.
        
        E: type: None, None
    
        S: type: None, None
        """
        messagebox.showerror("Erreur", "Veuillez prendre en considération les recommations sur la sécurité de votre mot de passe s'il vous plait.") #popup erreur
        mdp_entry.delete(0, tk.END) #Supprime le contenu de l'entrée.
        mdp_entry.config(validate = 'key', validatecommand = (validate_command, '%P')) #Redéfini l'argument permétant d'appliquer la vérification à chaque enfoncement de touche dans l'entry et la commande de vérification.
    

    def mdpGet():
        """Affiche la force du mot de passe.
        
        E: type: None, None
    
        S: type: None, None
        """
        
        Mdp = mdp_entry.get() #On obtient ce qui est écrit dans l'entrée.
        
        retourForce = TestForce(Mdp) #Effectue le test de force.
        
        labForce.config(text=f"Votre force de mot de passe est de {retourForce}/20.") #On change la force affichee.
        
        print(GrapheTest()) #Lance la fonction qui fait le graphe.


    root = tk.Tk() #Crée une fenêtre avec Tkinter.
    frm = tk.ttk.Frame(root, padding=10) #Crée un cadre.
    frm.grid() #On organise le cadre avec une grille.
    
    #Convertir la forme de la fonction
    validate_command = root.register(validation) #On passe la commande de vérification sous la bonne forme pour que tkinter puisse l'utiliser.
    

    tk.ttk.Label(frm, text="Force du mot de passe").grid(column=0, row=0) #Une étiquette.
    tk.ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) #Bouton pour détruire la fenêtre.
    
    mdp_entry = tk.Entry(frm, text="Mot de passe.", validate = 'key', validatecommand = (validate_command, '%P')) #On crée l'entrée.
    mdp_entry.grid(column=0, row=1) #Place l'entrée dans l'endroit de la grille voulu.
    
    tk.ttk.Button(frm, text="Force du mot de passe",command=lambda: mdpGet()).grid(column=1, row=1) #Bouton pour effectuer le test.
    
    labForce = tk.ttk.Label(frm, text=f"Votre force de mot de passe est de [?]/20.")#Affiche une étiquette sur laquelle est donnée la force du mot de passe.
    labForce.grid(column=0, row=2) # Organise sur la grille.
    
    #BoucleBase
    root.mainloop()
    

def tkinter2():
    """Générateur de mot de passe.
    
    E: type: None, None
    
    S: type: None, None
    """
    
    def optionsGet():
        """Lance le générateur de mot de passe avec les arguments choisis par l'utilisateur.
        
        E: type: None, None
    
        S: type: None, None
        """
        Longueur = int(ChoixLongueur.get()) #On récupère les arguments écrits dans les entrées.
        Nombre = int(NombreDeMots.get())
        print(Generateur(Longueur, Nombre)) #Effectue l& génération du mot de passe.
        Label_result.config(text = f"Votre mot de passe est {GenerationMdp}.")
    
    GenerateurTKinter = tk.Tk() #Créer une fenêtre.
    frm = tk.ttk.Frame(GenerateurTKinter, padding=10) #Crée un cadre.
    frm.grid() #On organise le cadre avec une grille.
    
    tk.ttk.Label(frm, text="Generateur").grid(column=0, row=0) #Etiquette.
    
    tk.ttk.Button(frm, text="Quit", command=GenerateurTKinter.destroy).grid(column=1, row=0) #Bouton pour détruire la fenêtre.
    
    ChoixLongueur = tk.Entry(frm, text="Longueur des mots") #On crée une entrée.
    ChoixLongueur.grid(column=0, row=1) #Organise dans la grille.
    
    NombreDeMots = tk.Entry(frm, text="Nombre de mots") #On crée une entrée.
    NombreDeMots.grid(column=0, row=2) #Organise dans la grille.
    
    tk.ttk.Label(frm, text="Longueur des mots").grid(column=1, row=1) #Etiquette.
    
    tk.ttk.Label(frm, text="Nombre de mots").grid(column=1, row=2) #Etiquette.
    
    tk.ttk.Button(frm, text="Valider", command=lambda: optionsGet()).grid(column=1, row=3) #Bouton lançant la génération.
    
    Label_result = tk.ttk.Label(frm, text=f"Votre mot de passe est [?].") #Etiquette qui affiche le mot de passe.
    Label_result.grid(column=0, row=3)
    
    #BoucleBase
    GenerateurTKinter.mainloop()
    

def tkinterHome():
    """Fenêtre principale.
    
    E: type: None, None
    
    S: type: None, None
    """
    def FonctionnaliteGet():
        """Renvoie vers les autres fenêtres avec le choix de l'utilisateur.
        
        E: type: None, None
    
        S: type: None, None
        """
        ChoixUtilisateur = int(ChoixUser.get()) #Récupère le choix.
        
        if ChoixUtilisateur == 0: #Condition, si l'utilisateur a choisi d'aller sur le test ou le générateur.
            
            print(tkinter()) #Test de force
            
        else:
            
            print(tkinter2()) #Générateur
            
    Home = tk.Tk() #Crée la fenêtre.
    
    frm = tk.ttk.Frame(Home, padding=10) #Crée un cadre.
    frm.grid() #On organise le cadre avec une grille.
    
    tk.ttk.Label(frm, text="Gestionnaire de mots de passe").grid(column=0, row=0) #Etiquette.
    
    tk.ttk.Label(frm, text="Test de force = 0, Generateur de mot de passe = 1").grid(column=1, row=1) #Etiquette
    
    tk.ttk.Button(frm, text="Quit", command=Home.destroy).grid(column=1, row=0) #Bouton pour détruire la fenêtre.
    
    ChoixUser = tk.Entry(frm, text="Fonctionnalite") #On crée une entrée pour choisir ou aller.
    ChoixUser.grid(column=0, row=1) #Organise dans la grille.
    
    tk.ttk.Button(frm, text="Valider", command=lambda: FonctionnaliteGet()).grid(column=1, row=3) #Bouton pour se déplacer.
    
    #BoucleBase
    Home.mainloop()


#Generateur de mot de passe
def Generateur(Longueur, Nombre):
    """Générateur de mot de passe.

    Args:
        Longueur (int): Longueur des mots du mot de passe.
        Nombre (int): Nombre de mots dans le mot de passe.

    Returns:
        str: ""
    """

    global GenerationMdp #On peut l'utiliser dans d'autres fonctions.
    GenerationMdp = "" #Définir la variable.
    
    ListeFrancais = open('liste_francais.txt', encoding = "ISO-8859-1") #Ouvre la liste des mots francais.
        
    ListeFrancais = ListeFrancais.read().split() #Lit et divise la liste.
        
    for _ in range(Nombre): #Le nombre de mots dans le mot de passe.
            
        #Prend une premiere lettre aleatoirement dans l'alphabet
        PremiereLettre = random.choice(alphabet)
            
        #Fais une liste de tous les mots qui commencent par la premiere lettre puis selectionne un des mots aleatoirement
        ListePremiereLettre = [mot for mot in ListeFrancais if mot.lower().startswith(PremiereLettre)]
            
        MotSuivant = random.choice(ListePremiereLettre) # Le mot est decide aleatoirement parmi les mots selectionnes.
            
        #Limite le nombre de caracteres pris dans le mot
        MotSuivant = MotSuivant[:Longueur]
            
        print(MotSuivant) #Affiche le mot suivant.
            
        GenerationMdp = GenerationMdp + (MotSuivant) + "-" #Mot de passe.
        
    return ("") # Ne retourne rien.



#Test de force
def TestForce(Mdp):
    """_Ce programme teste la force d'un mot de passe saisi par l'utilisateur._
    
    Args:
    Mdp (str): Mot de passe.

    Returns:
        _str_: _Donne la force du mot de passe._
    """
    global MdpUser
    MdpUser = str(Mdp)
    global Force
    Force = 0
    Fchiffres = 0
    
    for _ in MdpUser: #Rajoute 0.5 à force pour chaque caractère.
        Force += 0.5
        
    global Frequence
    Frequence = Counter(MdpUser) #Crée un dictionnaire de couples caractères - fréquence des caractères.
        
    for lettre, count in Frequence.items(): #Pour touts les caractères du mot de passe.
            
        if count > 1: #Si la fréquence du caractère est plus grande que 1.
            Force -= (count - 1) #Diminuer la force de 1 pour chaque caractère en trop dans la fréquence d'un caractère.

    for lettre in MdpUser: #Balaye touts les caractères du mot de passe.
        if lettre in string.ascii_uppercase: #Si le caractère se trouve dans la chaîne de caractère de toutes les lettres majuscules.
            Force += 1
            
        elif lettre in chiffres: #Si au moins un des caractères est un chiffre.
            Fchiffres = 2
            
        elif lettre in punctuation: #Si au moins un des caractères fait partie de la collection non ordonnée des ponctuations.
            Force += 1
            
    if len(MdpUser) < 5: #S'il y a moins de 5 caractères dans le mot de passe.
        for _ in range(4 - len(MdpUser)): #Pour chaque caractère qui manque pour avoir 5 caractères.
            Force -= 1

    Force += Fchiffres #Ajoute la valeur de Fchiffres à Force, s'il y a des chiffres on rajoute 2 sinon 0.
    
    if Force > 20: #Défini la note à la note maximale si le mot de passe a eu plus de 20 points.
        Force = 20
    elif Force < 0: #Si le mot de passe est en dessous de zéro la force du mot de passe prend la valeur de la note minimale, 0.
        Force = 0
        
    return(Force) #Retourne la force.
        
  
  
  
  
def GrapheTest():
    """On crée un graphique et on en fait une image qu'on enregistre.
    
    E: type: None, None
    
    S: type: None, None
    """
    CarX = sorted(set(MdpUser), key=MdpUser.index) #Liste de l'axe x. Cette liste est composée de caractères présents une fois seulement. On crée un set MdpUser pour supprimmer les caractères en double ou plus puis on crée une liste triée avec les caractères du set placés dans la liste en fonction de leut indice dans la chaîne de caractères initiale.
    FreqY = [Frequence[lettre] for lettre in CarX] #Liste de l'axe y. Liste des fréquences du dictionnaire pour toutes les clés de ce même dictionnaire dans la liste triée Carx.
    
    plt.figure(figsize = (8, 8)) #Défini la taille du graphe.
    
    plt.title("Frequence des caracteres dans le mot de passe") #Donne un titre.
    
    plt.xlabel("Caracteres") #Etiquette de l'axe x.
    
    plt.ylabel("Frequence", rotation = 45) #Etiquette de l'axe y, tournée à 45 degrés pour permettre une lecture plus aisée.
    
    plt.xticks(range(len(CarX)), CarX, rotation = 45) #Les caractères sont affichés sur l'axe des abscisses.
    #On ne le fait pas pour l'axe y car Mathplotlib gère tout seul quand on utilise la liste FreqY en argument dans plt.plot ou plt.scatter.
    
    plt.legend(title = "Attention, les caractères dépassant la ligne pointillée se répètent beaucoup.", bbox_to_anchor = (0.5, -0.1), loc = "center") #Légende dont le centre est situé à une position x de 1/2 du graphique et à une position y de -1/10 du graphique.
    
    plt.plot(CarX, [3] * len(CarX), linestyle = "--", color = "red") #Ligne constante en y = 3.
    
    plt.plot(CarX, FreqY, linestyle = "-", color = "blue") #Ligne qui va de points en points en fonction des valeurs x et y des points du graphe.
    
    
    plt.scatter(CarX, FreqY, marker = "+", color = "green") #Crée des points pour chaque paire de valeurs.
    
    plt.savefig(r"C:\Users\anneg\Desktop\MotDePasse\Graphique.png") #Sauvegarde du graphique.
      
    
    #On ouvre l'image puis on la converti a un format que tkinter comprend mais si ca ne fonctionne pas on retourne un message d'erreur. Cela n'est utile que pour mieux avoir conscience d'ou peut se situer une erreur.
    try:
        
        image = Image.open(r"C:\Users\anneg\Desktop\MotDePasse\Graphique.png") #Ouvre l'image.
        
    except: # Si ca ne fonctionne pas.
        
        messagebox.showerror("Erreur", "Image non trouvée.") # Message d'erreur.
        
        return("Erreur") # Met fin a la fonction.
    
    photo = ImageTk.PhotoImage(image) #Converti l'image sous un format que tkinter comprend.
    
    afficher_graph_tkinter(photo) #On lance la fonction avec l'image en arguments.
    
def afficher_graph_tkinter(photo):
    """_Affiche le graphique sur une fenetre tkinter._

    Args:
        photo (_png_): _L'image du graphique._
    """
    graph = tk.Toplevel() #On crée une fenetre secondaire.
    graph.title("Graphique") #Titre
    
    label = tk.Label(graph, image = photo) #Une étiquette.
    label.config(image = photo) #On configure l'étiquette en concervant l'image pour éviter que le garbage collector de python ne la supprime.
    label.grid(column = 0, row = 0) #On organise l'étiquette.
    
    tk.ttk.Button(graph, command = graph.destroy, text = "Quit").grid(column = 1, row = 1) #Bouton pour quitter.
    
    
    
    graph.mainloop() #BoucleBase
    
  
  
#Choix utilisateur
print(tkinterHome())