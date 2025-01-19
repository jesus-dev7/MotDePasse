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

import customtkinter

import speech_recognition as sr

import pyttsx3

#Definition variables
alphabet = string.ascii_lowercase #Les caractères en minuscule.

AlphabetMaj = string.ascii_uppercase #Les caractères en majuscule.

ListePremiereLettre = []

MotSuivant = 0

set(punctuation) #Liste des caractères spéciaux.

chiffres = "0123456789" #Définition des chiffres sous forme d'une chaîne de caractères.

set(chiffres) #Liste des chiffres.

def TkinterCookies():
    
    PageCookies = tk.Tk() #Crée une fenêtre.

    frm = tk.Frame(PageCookies, bd = 5, relief = "ridge", bg = "Black") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    PageCookies.rowconfigure(0, weight=1) #Les widgets vont au centre de la fenêtre.
    
    PageCookies.columnconfigure(0, weight=1) #Les widgets vont au centre de la fenêtre.
      
    tk.Label(frm, text = "En appuyant sur le bouton 'Accepter ', vous acceptez", bg = "Black", fg = "Green").grid(column = 0, row = 0, sticky = "w") #Affiche les cookies.
    
    tk.Label(frm, text = "l'utilisation des cookies et acceptez de vendre vos informations ", bg = "Black", fg = "Green").grid(column = 0, row = 1, sticky = "w") #Affiche les cookies.
    
    tk.Label(frm, text = "personnelles à des gens qui se feront de l'argent sur votre dos.", bg = "Black", fg = "Green").grid(column = 0, row = 2, sticky = "w") #Affiche les cookies.
    
    tk.Button(frm, text="Refuser", command = PageCookies.destroy, bg = "Red").grid(column=1, row=3, sticky = "w") #Bouton pour détruire la fenêtre.
    
    tk.Button(frm, text="Accepter", command = lambda: AccptCookies(), bg = "Green").grid(column=0, row=3, sticky = "w") #Bouton pour détruire la fenêtre.
    
    global UserCookies_entry #On peut l'utiliser dans d'autres fonctions.
    
    tk.Label(frm, text="Votre nom d'utilisateur (Ne pas mettre d'accent)", bg = "Green", bd = 4, relief = "sunken").grid(column=2, row=2, sticky = "nsew") #Etiquette.
    
    UserCookies_entry = tk.Entry(frm, bg = "Lightgreen")
    
    UserCookies_entry.grid(column = 2, row = 3) #On crée l'entrée.
    
    def AccptCookies():
        
        global UserCookies_entry #On peut l'utiliser dans d'autres fonctions.
        
        global ContenuCookies #On peut l'utiliser dans d'autres fonctions.
        
        Cookies = open(r'C:\Users\anneg\Desktop\MotDePasse\ListeCookies.txt', encoding = "ISO-8859-1") #Ouvre la liste des cookies et users qui les ont acceptés.

        ContenuCookies = Cookies.read() #Crée un string avec le contenu du fichier.
        
        if UserCookies_entry.get() == "":
            
            messagebox.showerror("Erreur", "Veuillez entrer un nom d'utilisateur.") #Popup erreur.
            
        else:
            
            ContenuCookies += f"User {UserCookies_entry.get()} a accepte les cookies.\n" #Ajoute l'utilisateur à la liste des utilisateurs qui ont accepté les cookies.
            
            with open(r'C:\Users\anneg\Desktop\MotDePasse\ListeCookies.txt', 'w', encoding = "ISO-8859-1") as file:
                
                file.write(ContenuCookies) #Ecrit le contenu dans le fichier.
            
        PageCookies.destroy() #Détruit la fenêtre.
            
def tkinterTest():
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
        
        global retourForce
        
        retourForce = TestForce(Mdp) #Effectue le test de force.
        
        labForce.config(text=f"Votre force de mot de passe est de {retourForce}/20.") #On change la force affichee.
        
        print(ListeMdpUpgrade())
        
        print(GrapheTest()) #Lance la fonction qui fait le graphe.
        
    global NombreAffichage #On peut l'utiliser dans d'autres fonctions.
    
    NombreAffichage = 0 #Initialise le nombre d'affichages.
        
    def AfficheMDP():
        """Affiche le mot de passe.
        
        E: type: None, None
    
        S: type: None, None
        """
        
        global NombreAffichage #On fait référence à une variable définie en dehors de la fonction ce qui nous permet de la modifiée même si elle n'est pas définie dans la fonction.
        
        NombreAffichage += 1 #Ajoute 1 au nombre d'affichages.
        
        if NombreAffichage == 1:
            
            mdp_entry.config(show = "")
            
            OuvreOeuil()
            
        else:
            mdp_entry.config(show = "©")
            
            NombreAffichage = 0
            
            FermeOeuil()
            
        return("")

    root = tk.Tk() #Crée une fenêtre avec Tkinter.
    
    frm = tk.Frame(root, bd = 5, relief = "ridge", bg = "Black") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    root.rowconfigure(0, weight=1) #Les widgets vont au centre de la fenêtre.
    
    root.columnconfigure(0, weight=1) #Les widgets vont au centre de la fenêtre.
    
    #Convertir la forme de la fonction
    validate_command = root.register(validation) #On passe la commande de vérification sous la bonne forme pour que tkinter puisse l'utiliser.
    
    tk.Label(frm, text="Force du mot de passe", bg = "Orange", relief = "sunken", bd = 4).grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    UnBoutonQuit = tk.Button(frm, text="Quit", command=root.destroy, bg = "red", width = 5) #Bouton pour détruire la fenêtre.
    
    UnBoutonQuit.grid(column=1, row=3)
    
    global mdp_entry #On peut l'utiliser dans d'autres fonctions.
    
    mdp_entry = tk.Entry(frm, text="Mot de passe.", show = "⚠", validate = 'key', validatecommand = (validate_command, '%P'), bg = "Lightgreen", relief = "ridge", bd = 6, font = ("bold")) #On crée l'entrée.
    
    mdp_entry.grid(column=0, row=1, sticky = "nsew") #Place l'entrée dans l'endroit de la grille voulu.
    
    ForceDuMDPBtn = tk.Button(frm, text="Force du mot de passe",command=lambda: mdpGet(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #Bouton pour effectuer le test.
    
    ForceDuMDPBtn.grid(column=1, row=0)
    
    labForce = tk.Label(frm, text=f"Votre force de mot de passe est de [?]/20.", bg = "Orange", relief = "sunken", bd = 4)#Affiche une étiquette sur laquelle est donnée la force du mot de passe.
    
    labForce.grid(column=0, row=2, sticky = "nsew") # Organise sur la grille.
    
    global imageOuvert #On peut l'utiliser dans d'autres fonctions.
    
    imageOuvert = Image.open(r"OeuilOuvert.jpg") #Ouvre l'image.
    
    imageOuvert = imageOuvert.resize((30, 22)) #Redimensionne l'image.
    
    imageOuvert = ImageTk.PhotoImage(imageOuvert) #Convertit l'image sous un format que tkinter comprend.
    
    global imageOeuilFerme #On peut l'utiliser dans d'autres fonctions.
    
    imageOeuilFerme = Image.open(r"OeuilFerme.jpg") #Ouvre l'image.
    
    imageOeuilFerme = imageOeuilFerme.resize((30, 22)) #Redimensionne l'image.
    
    imageOeuilFerme = ImageTk.PhotoImage(imageOeuilFerme) #Convertit l'image sous un format que tkinter comprend.
    
    Bouton_oeuil = tk.Button(frm, image = imageOeuilFerme, command=lambda: AfficheMDP(), bg = "Blue", relief = "ridge", bd = 4, width = 20, height = 12)#Bouton pour afficher le mot de passe.
    
    Bouton_oeuil.image = imageOeuilFerme #On conserve l'image pour éviter que le garbage collector de python ne la supprime.
    
    Bouton_oeuil.grid(column=1, row=1, sticky = "w") #Organise sur la grille.
    
    VocTest = tk.Button(frm, text="Vocal",command=lambda: GenerationVocale3(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #Bouton pour effectuer le test.
    
    VocTest.grid(column=1, row=2, sticky = "nsew")
    
    global Propositions
    
    Propositions = tk.Label(frm, text="", bg = "Orange", relief = "sunken", bd = 4)
    
    Propositions.grid(column=0, row=3, sticky = "nsew") #Etiquette.
    
    def Lire_BoutonVocTest_():
    
        def __LireContenu1_____(VocTest):
        
            contenu = VocTest.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        VocTest.bind("<Enter>", __LireContenu1_____)
    
    Lire_BoutonVocTest_()
    
    def Lire_BoutonVocTestQuit_():
    
        def __LireContenu2_____(UnBoutonQuit):
        
            contenu = UnBoutonQuit.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        UnBoutonQuit.bind("<Enter>", __LireContenu2_____)
    
    Lire_BoutonVocTestQuit_()
    
    def Lire_BoutonVocTestForce_():
    
        def __LireContenu3_____(ForceDuMDPBtn):
        
            contenu = ForceDuMDPBtn.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        ForceDuMDPBtn.bind("<Enter>", __LireContenu3_____)
    
    Lire_BoutonVocTestForce_()
    
    def OuvreOeuil():
        """Ouvre l'oeil.
        
        E: type: None, None
    
        S: type: None, None
        """
        global image #On peut l'utiliser dans d'autres fonctions.
        
        Bouton_oeuil.config(image = imageOuvert)
        
    def FermeOeuil():
        """Ouvre l'oeil.
        
        E: type: None, None
    
        S: type: None, None
        """
        global imageOeuilFerme #On peut l'utiliser dans d'autres fonctions.
        
        Bouton_oeuil.config(image = imageOeuilFerme)

    #BoucleBase
    root.mainloop()
    

def tkinterGenerateur():
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
        
        print(Generateur(Longueur, Nombre)) #Effectue la génération du mot de passe.
        
        Label_result.config(text = f"Votre mot de passe est {GenerationMdp}.")
    
    GenerateurTKinter = tk.Tk() #Créer une fenêtre.
    
    frm_ = tk.Frame(GenerateurTKinter, bd = 5, relief = "ridge", bg = "Black") #Crée un cadre.
    
    frm_.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    frm_.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    frm_.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    GenerateurTKinter.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    GenerateurTKinter.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    tk.Label(frm_, text="Generateur", bg = "Orange", relief = "sunken", bd = 4).grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    UnBoutonDeDestruction = tk.Button(frm_, text="Quit", command=GenerateurTKinter.destroy, bg = "red") #Bouton pour détruire la fenêtre.
    
    UnBoutonDeDestruction.grid(column=0, row=4, sticky = "nsew") #Bouton pour détruire la fenêtre.
    
    global ChoixLongueur #On peut l'utiliser dans d'autres fonctions.
    
    global NombreDeMots #On peut l'utiliser dans d'autres fonctions.
    
    ChoixLongueur = tk.Entry(frm_, text="Longueur des mots", bg = "Lightgreen", fg = "red", relief = "ridge", bd = 6, font = ("bold")) #On crée une entrée.
    
    ChoixLongueur.grid(column=0, row=1, sticky = "nsew") #Organise dans la grille.
    
    NombreDeMots = tk.Entry(frm_, text="Nombre de mots", bg = "Lightgreen", fg = "red", relief = "ridge", bd = 6, font = ("bold")) #On crée une entrée.
    
    NombreDeMots.grid(column=0, row=2, sticky = "nsew") #Organise dans la grille.
    
    tk.Label(frm_, text="Longueur des mots", bg = "Orange", relief = "ridge", bd = 4).grid(column=1, row=1, sticky = "ew") #Etiquette.
    
    tk.Label(frm_, text="Nombre de mots", bg = "Orange", relief = "ridge", bd = 4).grid(column=1, row=2, sticky = "ew") #Etiquette.
    
    global BTN_Valid
    
    BTN_Valid = tk.Button(frm_, text="Valider", command=lambda: optionsGet(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #Bouton lançant la génération.
    
    BTN_Valid.grid(column=1, row=0, sticky = "nsew")
    
    Label_result = tk.Label(frm_, text=f"Votre mot de passe est [?].", bg = "Orange", relief = "sunken", bd = 4) #Etiquette qui affiche le mot de passe.
    
    Label_result.grid(column=0, row=3, sticky = "nsew")
    
    Voc1_Gen = tk.Button(frm_, text="Vocal", command=lambda: GenerationVocale(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #Bouton lançant la génération.
    
    Voc1_Gen.grid(column=1, row=3, sticky = "nsew")
    
    Voc2_Gen = tk.Button(frm_, text="Vocal Champ 2", command=lambda: GenerationVocale2(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #Bouton lançant la génération.
    
    Voc2_Gen.grid(column=1, row=4, sticky = "nsew")
    
    def Lire_BoutonValider_():
    
        def LireContenu_____(BTN_Valid):
        
            contenu = BTN_Valid.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        BTN_Valid.bind("<Enter>", LireContenu_____)
    
    Lire_BoutonValider_()
    
    def Lire_BoutonQuit_():
    
        def _LireContenu_____(UnBoutonDeDestruction):
        
            contenu = UnBoutonDeDestruction.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        UnBoutonDeDestruction.bind("<Enter>", _LireContenu_____)
    
    Lire_BoutonQuit_()
    
    def Lire_BoutonVoc1_():
    
        def __LireContenu_____(Voc1_Gen):
        
            contenu = Voc1_Gen.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        Voc1_Gen.bind("<Enter>", __LireContenu_____)
    
    Lire_BoutonVoc1_()
    
    def Lire_BoutonVoc2_():
    
        def __LireContenu_____(Voc2_Gen):
        
            contenu = Voc2_Gen.widget.cget("text")
    
            engine.say(contenu)
    
            engine.runAndWait()
        
        engine = pyttsx3.init()
    
        Voc2_Gen.bind("<Enter>", __LireContenu_____)
    
    Lire_BoutonVoc2_()
    
    #BoucleBase
    GenerateurTKinter.mainloop()
    
def tkinterHome():
    """Fenêtre principale.
    
    E: type: None, None
    
    S: type: None, None
    """
    
    print(TkinterCookies()) #Affiche les cookies.
            
    Home = tk.Tk() #Crée la fenêtre.
    
    frm = tk.Frame(Home, bg = "Black", bd = 5, relief = "ridge") #Crée un cadre.
    
    frm.grid(padx = 10, pady = 10) #On organise le cadre avec une grille.
    
    frm.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    frm.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    Home.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    Home.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    global LabelGest
    
    global Bouton_
    
    LabelGest = tk.Label(frm, text="Gestionnaire de mots de passe", bg = "Orange", relief = "sunken") #Une étiquette.
    
    LabelGest.grid(column=0, row=0, sticky = "nsew") #Etiquette.
    
    Bouton_ = tk.Button(frm, text="Quit", command=Home.destroy, bg = "red") #Bouton pour détruire la
    
    Bouton_.grid(column=1, row=3, sticky = "nsew") #Bouton pour détruire la fenêtre.
    
    global ChoixUserTest #On peut l'utiliser dans d'autres fonctions.
    
    global ChoixUserGenerateur #On peut l'utiliser dans d'autres fonctions.
    
    global TradBtn
    
    ChoixUserGenerateur = tk.Button(frm, text="Générateur", command = lambda: tkinterGenerateur(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #On crée une entrée pour choisir ou aller.
    
    ChoixUserTest = tk.Button(frm, text="Test de force", command = lambda: tkinterTest(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic")) #On crée une entrée pour choisir ou aller.
    
    ChoixUserGenerateur.grid(column=0, row=1, sticky = "nsew", padx = 10, pady = 10) #Organise dans la grille.
    
    ChoixUserTest.grid(column=0, row=2, sticky = "nsew", padx = 10, pady = 10) #Organise dans la grille.
    
    TradBtn = tk.Button(frm, text="Traducteur", command = lambda: TkinterTrad(), bg = "Blue", fg = "red", font = ("Times New Roman", 10, "bold italic"))
    
    TradBtn.grid(column=0, row=3, sticky = "nsew", padx = 10, pady = 10) #Organise dans la grille.
    
    Home.after(2000, OralHome)
    
    Lire_BoutonGen()
    
    Lire_BoutonTest()
    
    Lire_BoutonTrad()
    
    Lire_BoutonQuit()
    
    #BoucleBase
    Home.mainloop()

def OralHome():
    
    def LireContenu():
        
        contenu = LabelGest.cget("text")
        
        engine.say(contenu)
        
        engine.runAndWait()
        
    engine = pyttsx3.init()

    LireContenu()

def Lire_BoutonGen():
    
    def LireContenu_(ChoixUserGenerateur):
        
        contenu = ChoixUserGenerateur.widget.cget("text")
    
        engine.say(contenu)
    
        engine.runAndWait()
        
    engine = pyttsx3.init()
    
    ChoixUserGenerateur.bind("<Enter>", LireContenu_)
    
def Lire_BoutonTest():
    
    def LireContenu__(ChoixUserTest):
        
        contenu = ChoixUserTest.widget.cget("text")
    
        engine.say(contenu)
    
        engine.runAndWait()
        
    engine = pyttsx3.init()
    
    ChoixUserTest.bind("<Enter>", LireContenu__)
    
def Lire_BoutonTrad():
    
    def LireContenu___(TradBtn):
        
        contenu = TradBtn.widget.cget("text")
    
        engine.say(contenu)
    
        engine.runAndWait()
        
    engine = pyttsx3.init()
    
    TradBtn.bind("<Enter>", LireContenu___)
    
def Lire_BoutonQuit():
    
    def LireContenu____(Bouton_):
        
        contenu = Bouton_.widget.cget("text")
    
        engine.say(contenu)
    
        engine.runAndWait()
        
    engine = pyttsx3.init()
    
    Bouton_.bind("<Enter>", LireContenu____)

def TkinterTrad():
    
    def EntryGetToText():
        
        global text
        
        if Entry.get("1.0", "end-1c") != "":
        
            text = Entry.get("1.0", "end-1c")
        
        Label.configure(text = "'" + AskToText() + "'")
    
    def EntryGetToAsk():
        
        global text
        
        if Entry.get("1.0", "end-1c") != "":
        
            text = Entry.get("1.0", "end-1c")
        
        Label.configure(text = TextToAsk())
    
    main = customtkinter.CTk() #Crée une fenêtre.
    
    main.title("Traducteur") #Titre de la fenêtre.
    
    main.resizable(False, False) #On ne peut pas redimensionner la fenêtre.
    
    customtkinter.CTkLabel(main, text = "Traducteur").grid(column = 1, row = 0, pady = (10, 10), padx = (10, 10)) #Etiquette.
    
    Entry = customtkinter.CTkTextbox(main, width = 200, height = 10) #Zone de texte.
    
    Entry.grid(column = 1, row = 1, pady = (10, 10), padx = (10, 10))
    
    customtkinter.CTkButton(main, text = "ASCII à texte", command = lambda: EntryGetToText()).grid(column = 1, row = 2, pady = (10, 10), padx = (10, 10)) #Bouton pour traduire.
    
    customtkinter.CTkButton(main, text = "Texte à ASCII", command = lambda: EntryGetToAsk()).grid(column = 1, row = 3, pady = (10, 10), padx = (10, 10)) #Bouton pour traduire.
    
    customtkinter.CTkButton(main, text = "Quit", command = main.destroy).grid(column = 1, row = 4, pady = (10, 10), padx = (10, 10)) #Bouton pour traduire.
    
    Label = customtkinter.CTkLabel(main, text = "") #Etiquette.
    
    Label.grid(column = 4, row = 0, pady = (10, 10), padx = (10, 10))
    
    Label = customtkinter.CTkLabel(main, text = "Separer chaque code ASCII par 47") #Etiquette.
    
    Label.grid(column = 3, row = 1, pady = (10, 10), padx = (10, 10))
    
    main.mainloop()
    
def ListeMdpUpgrade():
    
    if retourForce <= 10:
        
        ListeMdpAternative = []
        
        MdpOrigine = mdp_entry.get()
        
        UnCompteurPunct = 0
        
        UnCompteurChiffres = 0
        
        UnCompteurMaj = 0
        
        for UnIndexLettre in MdpOrigine:
            
            if UnIndexLettre in punctuation:
                
                UnCompteurPunct += 1
                
            if type(UnIndexLettre) == int:
                
                UnCompteurChiffres += 1
                
            if UnIndexLettre in AlphabetMaj:
                
                UnCompteurMaj += 1
              
        MdpModif = ""  
              
        for _ in range(3):
            
            if UnCompteurPunct < 3:
            
                Indexrange = random.randint(1, 4)
            
                MdpModif = MdpOrigine
            
                for _ in range(Indexrange):
                
                    MdpModif += str(random.choice(punctuation))
                
            if UnCompteurChiffres < 3:
            
                Indexrange = random.randint(1, 3)
            
                for _ in range(Indexrange):
                
                    MdpModif += f"{random.randint(0, 9)}"
                
            if UnCompteurMaj < 3:
            
                Indexrange = random.randint(1, 3)
            
                for _ in range(Indexrange):
                
                    MdpModif += random.choice(AlphabetMaj)
            
            ListeMdpAternative.append(MdpModif)
        
        Propositions.config(text = f"{ListeMdpAternative}")
    
def GenerationVocale():
    
    def listen_convert():
        
        reconnaitre = sr.Recognizer() #Objet qui detecte et reconnait la parole.
        
        mic = sr.Microphone()
        
        with mic as source:
            
            print("Parlez...")
            
            reconnaitre.adjust_for_ambient_noise(source)
            
            audio = reconnaitre.listen(source)
            
        try:
            
            global paroles_crypt
            
            global paroles
            
            paroles = ""
            
            paroles_crypt = ""
            
            print("Reconnaissance vocale en cours...")

            paroles = reconnaitre.recognize_google(audio, language = "fr-FR")
            
            ChoixLongueur.insert(tk.END, str(paroles))
            
            print(f"paroles detectees {paroles}")
            
            return paroles
        
        except sr.UnknownValueError:
            
            print("Google speech recognition n'a pas pu comprendre l'audio.")
            
            return("")
        
        except sr.RequestError:
            
            print("Impossible d'obtenir une reponse de google speech recognition.")
            
            return("")
        
    def ecrire_dans_le_fichier():
        
        if paroles:
            
            paroles_crypt = ""
            
            for lettre in paroles:
                
                paroles_crypt += str(bin(ord(lettre)))
                
            print(paroles_crypt)
            
            with open(r"C:\Users\anneg\Desktop\MotDePasse\Données_Détection_Vocale.txt", "a", encoding = "UTF-8") as file:
                
                file.write(paroles_crypt + "\n")
                
            print("Texte crypte ecrit dans le fichier.")
        
        else:
            
            print("Rien a ecrire")
    
    listen_convert()
    
    ecrire_dans_le_fichier()
    
def GenerationVocale2():
    
    def listen_convert2():
        
        reconnaitre2 = sr.Recognizer() #Objet qui detecte et reconnait la parole.
        
        mic2 = sr.Microphone()
        
        with mic2 as source:
            
            print("Parlez...")
            
            reconnaitre2.adjust_for_ambient_noise(source)
            
            audio2 = reconnaitre2.listen(source)
            
        try:
            
            global paroles_crypt2
            
            global paroles2
            
            paroles2 = ""
            
            paroles_crypt2 = ""
            
            print("Reconnaissance vocale en cours...")

            paroles2 = reconnaitre2.recognize_google(audio2, language = "fr-FR")
            
            NombreDeMots.insert(tk.END, str(paroles2))
            
            print(f"paroles detectees {paroles2}")
            
            return paroles2
        
        except sr.UnknownValueError:
            
            print("Google speech recognition n'a pas pu comprendre l'audio.")
            
            return("")
        
        except sr.RequestError:
            
            print("Impossible d'obtenir une reponse de google speech recognition.")
            
            return("")
        
    def ecrire_dans_le_fichier2():
        
        if paroles2:
            
            paroles_crypt2 = ""
            
            for lettre___ in paroles2:
                
                paroles_crypt2 += str(bin(ord(lettre___)))
                
            print(paroles_crypt2)
            
            with open(r"C:\Users\anneg\Desktop\MotDePasse\Données_Détection_Vocale.txt", "a", encoding = "UTF-8") as file:
                
                file.write(paroles_crypt2 + "\n")
                
            print("Texte crypte ecrit dans le fichier.")
        
        else:
            
            print("Rien a ecrire")
    
    listen_convert2()
    
    ecrire_dans_le_fichier2()
    
def GenerationVocale3():
    
    def listen_convert3():
        
        reconnaitre3 = sr.Recognizer() #Objet qui detecte et reconnait la parole.
        
        mic3 = sr.Microphone()
        
        with mic3 as source:
            
            print("Parlez...")
            
            reconnaitre3.adjust_for_ambient_noise(source)
            
            audio3 = reconnaitre3.listen(source)
            
        try:
            
            global paroles_crypt3
            
            global paroles3
            
            paroles3 = ""
            
            paroles_crypt3 = ""
            
            print("Reconnaissance vocale en cours...")

            paroles3 = reconnaitre3.recognize_google(audio3, language = "fr-FR")
            
            mdp_entry.insert(tk.END, str(paroles3))
            
            print(f"paroles detectees {paroles3}")
            
            return paroles3
        
        except sr.UnknownValueError:
            
            print("Google speech recognition n'a pas pu comprendre l'audio.")
            
            return("")
        
        except sr.RequestError:
            
            print("Impossible d'obtenir une reponse de google speech recognition.")
            
            return("")
        
    def ecrire_dans_le_fichier3():
        
        if paroles3:
            
            paroles_crypt3 = ""
            
            for _lettre___ in paroles3:
                
                paroles_crypt3 += str(bin(ord(_lettre___)))
                
            print(paroles_crypt3)
            
            with open(r"C:\Users\anneg\Desktop\MotDePasse\Données_Détection_Vocale.txt", "a", encoding = "UTF-8") as file:
                
                file.write(paroles_crypt3 + "\n")
                
            print("Texte crypte ecrit dans le fichier.")
        
        else:
            
            print("Rien a ecrire")
    
    listen_convert3()
    
    def CaracSpeciaux():
        
        text = mdp_entry.get()
        
        print(f"TEXT : {text}")
        
        Remplacements = {"Inter" : "?",
                         "espère" : "&",
                         "base" : "@",
                         "Crush" : "["}
        
        for mot, caractere in Remplacements.items():
            
            text = text.replace(mot, caractere)
            
        print(f"TEXT MODIF: {text}")
            
        mdp_entry.delete(0, tk.END)
        
        mdp_entry.insert(0, text)
            
    CaracSpeciaux()
    
    ecrire_dans_le_fichier3()
    
def TextToAsk():
    
    ListeLettresAsk = [ord(lettre) for lettre in text]
    
    return(ListeLettresAsk)

def AskToText():
    
    Str = ""
    
    global text
    
    text = str(text)
    
    DiviseurAsk = ord("/")
    
    DiviseurStr = str(DiviseurAsk)
    
    NewList = text.split(DiviseurStr)
    
    NewList = [item for item in NewList if item != "" and item != " "]
    
    for element in range(len(NewList)):
        NewList[element] = int(NewList[element])
    
    for Ask in NewList:
        Str += chr(Ask)
        
    return Str
        
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
        
        Nombre = int(Nombre) #On convertit le nombre en entier.
        
        global ListePremiereLettre #On peut l'utiliser dans d'autres fonctions.
        
        ListePremiereLettre = [mot for mot in ListeFrancais if mot.lower().startswith(PremiereLettre) and len(mot) == Longueur] #Liste des mots qui commencent par la première lettre et qui ont la longueur voulue.
           
        if len(ListePremiereLettre) != 0: #Si la liste n'est pas vide.
         
            MotSuivant = random.choice(ListePremiereLettre) # Le mot est decide aleatoirement parmi les mots selectionnes.
            
        else:
            
            messagebox.showerror("Erreur", "Il n'y a pas assez de mots de cette longueur commençant par cette lettre. Veuillez réessayer ou changer les paramètres.") #Popup erreur.
            
        print(MotSuivant) #Affiche le mot suivant.
            
        GenerationMdp = GenerationMdp + (MotSuivant) + "-" #Mot de passe.
    
    GenerationMdp = GenerationMdp[:-1] #On enlève le dernier tiret.
    
    return (GenerationMdp) #Retourne le mot de passe.

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
        
        if lettre in AlphabetMaj: #Si le caractère se trouve dans la chaîne de caractère de toutes les lettres majuscules.
            
            Force += 1
            
        if lettre in chiffres: #Si au moins un des caractères est un chiffre.
            
            Fchiffres = 2
            
        if lettre in punctuation: #Si le caractères fait partie de la collection non ordonnée des ponctuations.
            
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
    
    plt.savefig(r"Graphique.png") #Sauvegarde du graphique.
      
    
    #On ouvre l'image puis on la convertit a un format que tkinter comprend mais si ca ne fonctionne pas on retourne un message d'erreur. Cela n'est utile que pour mieux avoir conscience d'ou peut se situer une erreur.
    try:
        
        image = Image.open(r"Graphique.png") #Ouvre l'image.
        
    except: # Si ca ne fonctionne pas.
        
        messagebox.showerror("Erreur", "Image non trouvée.") # Message d'erreur.
        
        return("Erreur") # Met fin a la fonction.
    
    photo = ImageTk.PhotoImage(image) #Convertit l'image sous un format que tkinter comprend.
    
    print(type(photo))
    
    afficher_graph_tkinter(photo) #On lance la fonction avec l'image en arguments.
    
    return("")
    
def afficher_graph_tkinter(photo):
    """_Affiche le graphique sur une fenetre tkinter._

    Args:
        photo (_png_): _L'image du graphique._
    """
    graph = tk.Toplevel(bg = "Black") #On crée une fenetre secondaire.
    
    graph.title("Graphique") #Titre

    graph.rowconfigure(0, weight=1) #On configure la ligne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    graph.columnconfigure(0, weight=1) #On configure la colonne 0 pour qu'elle s'adapte à la taille de la fenêtre.
    
    label = tk.Label(graph, image = photo, bg = "Orange", relief = "ridge", bd = 10) #Une étiquette.
    
    label.config(image = photo) #On configure l'étiquette en concervant l'image pour éviter que le garbage collector de python ne la supprime.
    
    label.grid(column = 0, row = 0) #On organise l'étiquette.
    
    tk.Button(graph, command = graph.destroy, text = "Quit", bg = "red", width = 5, height = 1, relief = "ridge", bd = 4).grid(column = 1, row = 1) #Bouton pour quitter.
    
    graph.mainloop() #BoucleBase
    
#Choix utilisateur
print(tkinterHome())