#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       gestion-boucfab.py
#       version 2.5
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc62>
#


# ----------------------------------------------------------------------
# @ FONCTIONS UTILES
# ----------------------------------------------------------------------
import os


# Cette fonction permet d'utiliser des énumerations
def enum(**enums):
    return type('Enum', (), enums)


def AfficherCoefficientsCertitude() :
    print("""\n\t\t\tCOEFFICIENTS DE CERTITUDE\n
------------------------------------------------------------------------
| Probabilité d'être sûr | Coefficient |     Bonne     |    Mauvaise   |
|     de la réponse      |             |    réponse    |    réponse    |
------------------------------------------------------------------------
|                        |             |               |               |
|   Entre 0 % et 25 %    |      0      |      +15      |      +4       |
|   Entre 25 % et 50 %   |      1      |      +16      |      +3       |
|   Entre 50 % et 70 %   |      2      |      +17      |      +2       |
|   Entre 70 % et 85 %   |      3      |      +18      |      0        |
|   Entre 85 % et 95 %   |      4      |      +19      |      -6       |
|   Entre 95 % et 100 %  |      5      |      +20      |      -20      |
|                        |             |               |               |
------------------------------------------------------------------------
\n""");



# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
def AfficherTutoriel() :
    print("""Bienvenue au QCM SJB version 2.5 !
    
Ce QCM dispose de quatre réponses implicites, c'est-à-dire qu'elles
ne seront pas affichées lorsque vous repondrez aux questions.
Les quatre réponses implicites sont les suivantes :
   d) Aucune
   e) Manque
   f) Absurde
   g) Toutes\n
   
Vous avez aussi la possibilité de passer les questions en répondant
par 'x' (ou 'X') et d'y répondre éventuellement à la fin du qcm.\n""");

    input("Appuyer sur Entrée ...");
    os.system("clear");
    
    print("""Ce QCM dispose aussi de coefficients de certitude.
À chaque question, plusieurs coefficients de certitude seront proposés :""");
    AfficherCoefficientsCertitude();
    
    input("Appuyer sur Entrée pour commencer le QCM ...");


def InitialiserQCM(nomFichier) :
    # Initialisation de la liste principale qui contiendra
    # toutes les questions, réponses etc. du fichier
    QCM = [];

    # Ouvre le fichier avec les questions
    fichierQCM = open(nomFichier, 'r');
    
    # Boucle qui lit le fichier ligne par ligne
    for ligne in fichierQCM :
        # Stocke la ligne découpée
        ligne = ligne.split('|');
        
        # Stocke la question
        question = ligne[0].strip();
        
        # Stocke les réponses de la question
        reponses = ligne[1].split(',');
        for i in range(len(reponses)) :
            reponses[i] = reponses[i].strip();

        # Stocke la bonne réponse
        bonneReponse = ligne[2].strip();
                
        # Ajoute la question, les réponses et la bonne réponse dans une
        # sous-liste, qui à son tour est ajoutée dans la liste principale
        QCM.append([question, reponses, bonneReponse]);
    
    # Ferme le fichier avec les questions
    fichierQCM.close();
    
    return QCM;


def AfficherQuestion(question) :
    # 1) Affichage de la question
    print(question[0]);
    
    # 2) Affichage des différentes réponses
    # À chaque réponse une lettre est attribuée
    lettres = "abcdefg";
    reponses = question[1];
    for cptReponses in range(len(reponses)) :
        print(" ({}) {}".format(lettres[cptReponses], reponses[cptReponses]));
        

def AfficherQuestionQCM(question, idQuestion, titre = "") :
    # Dictionnaire contenant les réponses que l'utilisateur peut donner
    reponsesDisponibles = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
                           'g':7, 'X':0, 'x':0};    
    
    # Liste contenant les coefficients de certitude que l'utilisateur
    # peut donner comme réponse
    coefficientsDisponibles = ['0', '1', '2', '3', '4', '5'];   
    
    # Énumération qui servent à gérer l'affichage des exceptions
    Donnees = enum(ReponseInvalide=1, CoefficientInvalide=2, Valides=3);
    
    # Valeur attribuée par défaut à un type énumération
    donnees = None;

    niveauAffichage = 1;
    while (niveauAffichage < 3) :
        os.system("clear");
        # 1) Affichage de l'en-tête
        print("{}\n".format(titre));
        
        # 2) Affichage de la question et des réponses
        print("Question n°{} : ".format(idQuestion), end="");
        AfficherQuestion(question);
            
        # 2a) Affichage des messages d'erreurs s'il y en a
        if (donnees == Donnees.ReponseInvalide) :
            print("La réponse que vous avez donnée est invalide");      
        elif (donnees == Donnees.CoefficientInvalide) :
            print("Le coefficient de certitude que vous avez entré est invalide.");
        
        # 3) Demander à l'utilisateur quelle est la bonne réponse
        if (niveauAffichage == 1) :
            reponse = input("La réponse est : ");
            if (not reponse in reponsesDisponibles) :
                donnees = Donnees.ReponseInvalide;
            elif (reponsesDisponibles[reponse] == 0) :
                coefficient = "";
                break;
            else :              
                donnees = Donnees.Valides;
                niveauAffichage += 1;               
            continue;
              
        # 4) Demander à l'utilisateur le coefficient de certitude  
        elif (niveauAffichage == 2) :
            print("La réponse est : {}".format(reponse));
            
            coefficient = input("Coefficient de certitude [ 0 | 1 | 2 | 3 | 4 | 5 ] : ");
            if (not coefficient in coefficientsDisponibles) :
                donnees = Donnees.CoefficientInvalide;              
            else :
                donnees = Donnees.Valides;
                niveauAffichage += 1;           
            continue;

    # 5) Renvoie les réponses de l'utilisateur et les coefficients de certitude
    #    à l'interieur d'un tuple
    return (reponsesDisponibles[reponse], coefficient);


def AfficherQuestionManquee(question, idQuestion) :
    os.system("clear");
    bonneReponse = int(question[2]);
    
    print(" - QUESTIONS MANQUÉES - ");
    
    # 1) Affichage de la question
    print("\nQuestion n°{} : {}".format(idQuestion, question[0]));    
    
    # 2) Création d'une copie (pas une réference) des réponses
    # de la question
    temp = []
    temp.extend(question[1]);
    # Les réponses implicites y sont ajoutées
    temp.extend(["Aucune", "Manque", "Absurde", "Toutes"]); 
            
    # Stocke la liste temporaire dans réponses
    reponses = temp;

    # 2) Affichage des réponses
    for cptReponses in range(len(reponses)) :
        # Si la réponse est une bonne réponse, afficher (*) à côté
        if (cptReponses+1 == bonneReponse) :
            print(" {} (*)".format(reponses[cptReponses]));
        else :
            print(" {}".format(reponses[cptReponses])); 


def AfficherScore(QCM, donneesUtilisateur) :
    # Données pour l'affichage du score
    nombreQuestions = len(QCM); 
    scoreUtilisateur = 0; # voir coefficients de certitude
    bonnesReponses = 0;
    mauvaisesReponses = 0;
    sansReponse = 0;
    
    ptsCoeffBonneReponse = {'0':15, '1':16, '2':17, '3':18, '4':19,
                            '5':20};
    ptsCoeffMauvaiseReponse = {'0':4, '1':3, '2':2, '3':0, '4':-6, 
                               '5':-20};
    # ------------------------------
        
    # Calcule le score
    for i in range(len(QCM)) :
        bonneReponse = int(QCM[i][2]);
        reponseUtilisateur = donneesUtilisateur[0][i];
        coefficientCertitude = donneesUtilisateur[1][i];    
        
        # Si la reponse de l'utilisateur était une bonne réponse ...
        if (reponseUtilisateur == bonneReponse) :
            # Renvoie le nombre de points correspondants au coefficient
            # proposé par l'utilisateur pour une bonne réponse et l'ajoute
            # au score de l'utilisateur
            scoreUtilisateur += ptsCoeffBonneReponse[coefficientCertitude];
            
            # Augmente de 1 le nombre de bonnes réponses
            bonnesReponses += 1;
            
        # En revanche ...
        else :
            # Si l'utilisateur a passé la question
            if (reponseUtilisateur == 0) :
                sansReponse += 1;
            # Si l'utilisateur a raté la question
            else :              
                # Renvoie le nombre de points correspondants au coefficient
                # proposé par l'utilisateur pour une mauvaise réponse et
                # l'ajoute au score de l'utilisateur
                scoreUtilisateur += ptsCoeffMauvaiseReponse[coefficientCertitude];
                
                # Augmente de 1 le nombre de mauvaises réponses
                mauvaisesReponses += 1; 

    # Affichage du score
    os.system("clear");
    print("""Resultat : \t\t\t\t{}
Bonnes réponses : \t\t\t{}
Mauvaises réponses : \t\t\t{}
Pas de réponse : \t\t\t{}
Nombre de questions : \t\t\t{}
""".format(scoreUtilisateur, bonnesReponses, mauvaisesReponses, sansReponse, nombreQuestions));



# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :
    monQCM = InitialiserQCM("questions.qsn");
    # Liste qui contient les données de l'utilisateur
    # - La première sous-liste contiendra les réponses de l'utilisateur
    # - La deuxième sous-liste contiendra les coefficients de certitude
    #   de l'utilisateur
    donneesUtilisateur = [[], []]

    # 1) Affichage du tutoriel
    AfficherTutoriel();
    
    
    # 2) Affichage des questions
    for cptQuestions in range(len(monQCM)) :
        temp = AfficherQuestionQCM(monQCM[cptQuestions], cptQuestions+1, " - QUESTIONS - ");
        donneesUtilisateur[0].append(temp[0]);
        donneesUtilisateur[1].append(temp[1]);
        input("\nQuestion suivante (Appuyer sur Entrée) ...");
    
    
    # 3) Affichage du score avant les questions passées
    AfficherScore(monQCM, donneesUtilisateur); 
    
    
    # 4) Affichage des questions passées
    # Calculer le nombre de questions passées et stocker leur index dans une liste
    questionsPassees = [];
    for cptQP in range(len(donneesUtilisateur[0])) :           
            if (donneesUtilisateur[0][cptQP] == 0) :
                questionsPassees.append(cptQP);
   
    # Si l'utilisateur a passé au moins une question ... (sinon ne rien faire)
    if (len(questionsPassees) != 0) :
        # Revoir les questions passées si l'utilisateur le désire et
        # réafficher le score ensuite
        revoirQP = input("Voulez-vous répondre aux questions passées (O/n) ? ");
        if (revoirQP == 'O' or revoirQP == 'o') :       
            for cptQuestions in range(len(questionsPassees)) :
                indexQuestion = questionsPassees[cptQuestions];             
                temp = AfficherQuestionQCM(monQCM[indexQuestion], indexQuestion+1, " - QUESTIONS PASSÉES - ");                
                donneesUtilisateur[0][indexQuestion] = temp[0];
                donneesUtilisateur[1][indexQuestion] = temp[1];
                input("\nQuestion suivante (Appuyer sur Entrée) ...");
        
        # Affichage du score après les questions passées
        AfficherScore(monQCM, donneesUtilisateur);
	
    
    # 5) Affichage des questions manquées
    # Calculer le nombre de questions manquées et stocker leur index dans une liste
    questionsManquees = [];
    for cptQM in range(len(donneesUtilisateur[0])) :           
            if (int(monQCM[cptQM][2]) != donneesUtilisateur[0][cptQM]) :
                questionsManquees.append(cptQM);
    
    # Si l'utilisateur a raté au moins une question ... (sinon ne rien faire)
    if (len(questionsManquees) != 0) :
        # Revoir les questions manquées si l'utilisateur le désire
        revoirQM = input("Voulez-vous revoir les questions manquées (O/n) ? ");
        if (revoirQM == 'O' or revoirQM == 'o') :
            for cptQuestions in range(len(questionsManquees)) :
                indexQuestion = questionsManquees[cptQuestions];                
                AfficherQuestionManquee(monQCM[indexQuestion], indexQuestion+1);
                input("\nQuestion suivante (Appuyer sur Entrée) ...");    
    
    print("\nFin du QCM ! Merci d'avoir participé ! ;)");
