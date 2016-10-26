#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       roulette-boucfab.py
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc55>
#


# ----------------------------------------------------------------------
# @ FONCTIONS UTILES
# ----------------------------------------------------------------------
from random import randrange
from random import shuffle
from sys import stdout
from sys import platform
from time import sleep
from os import system 

# On peut appeler la fonction "time.sleep" par "attendre()"
def attendre(secondes) :
    #pass
    sleep(secondes);


# On peut appeler la fonction pour effacer ce qu'il y a écrit dans
# la console par "effacerConsole()";
# La fonction se charge d'utiliser la bonne commande sur Windows et
# Linux
def effacerConsole() :
    if (platform == "win32") :
        system("cls");
    elif (platform == "linux2") :
        #os.system("clear");
        print("\033c");
    return;


# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
# Renvoie une liste où chaque indice contient un dictionnaire avec
# les informations sur un joueur
# Exemple : [ {"nom":"Joueur1", "portefeuille":1500}, { ... } ]
def creationJoueurs(joueurs) :
    # Somme d'argent que chaque joueur dispose avant de commencer le jeu
    argentDeBase = 1500;
    
    # Les noms des joueurs qu'ont joué la partie précedente sont stockés
    # dans une liste pour ne pas qu'il y ait des doublons ou un joueur
    # qui quitte et rejoint la partie suivante
    nomsJoueursPrecedents = [];
    
    # Enlever les joueurs qu'ont perdu la partie précedente
    i = 0;
    while i < len(joueurs) :
        nomsJoueursPrecedents.append(joueurs[i]["nom"]);
        if (joueurs[i]["perdu"] == True) :
            print("{} quitte la partie.".format(joueurs[i]["nom"]));
            del(joueurs[i]);
        else :
            i += 1;
        
        attendre(0.5);
        
    # Le nombre de joueurs est tiré aléatoirement
    nombreJoueursMin = 2;
    nombreJoueursMax = 8;
    nombreJoueurs = randrange(nombreJoueursMin, nombreJoueursMax+1) - len(joueurs);
    
    # Liste contenant différents prénoms à attribuer aux joueurs
    nomsJoueurs = ["Paul", "Jean-Yves", "Julien", "François", "Marco",
                   "Sasha", "Cyril", "Pauline", "Renaud", "Pierre",
                   "Jules", "Yannou", "Jerôme", "Fanny", "Guillaume",
                   "Fabio", "Jimmy"];
    
    # Grâce à la fonction shuffle, les éléments de la liste contenant
    # les prénoms sont mélangés aléatoirement. Ensuite, seulement un nombre
    # de prénoms correspondants au nombre de joueurs sera pris.
    shuffle(nomsJoueurs);
        
    i = -1;
    while (len(joueurs) < nombreJoueurs) :
         i += 1;
         # Dictionnaire qui contiendra les "attribus" de chaque
         # joueur (leur nom et l'argent qu'il possèdent)
         attribus = {};
         
         # Si le nom choisi est le même que celui d'un des joueurs qui
         # viennent de quitter, passer directement au nom suivant
         if (nomsJoueurs[i] in nomsJoueursPrecedents) :
             continue;
             
         attribus["nom"] = nomsJoueurs[i];
         attribus["portefeuille"] = argentDeBase;
         attribus["perdu"] = False;
         
         # Les attribus sont ajoutés à la liste principale
         joueurs.append(attribus);
         print("{} rejoint la partie.".format(nomsJoueurs[i]));
         attendre(0.5);      
    
    return joueurs;


# Se charge de créer une mise aléatoire pour chaque joueur, ensuite
# les informations (argent parié, type de mise ...) sont stockées
# dans le dictionnaire représentant le joueur
def gestionMises(joueurs) :
    # Chaque joueur va parier sur un nombre soit sur sa couleur ou
    # sur sa parité. Pour les joueurs 'IA' il faudra choisir cela
    # à l'avance.
    typeMiseIA = ["nombre", "couleur", "parité"];
    
    # L'ordre où les joueurs misent est aléatoire, pour rendre le jeu
    # plus réaliste.
    shuffle(joueurs);
    
    for joueur in joueurs :
        # Un joueur pur miser maximum la moitié de la valeur
        # totale de son portefeuille et minimum 1$
        miseMin = 1;
        miseMax = joueur["portefeuille"] // 2;
        
        joueur["mise"] = {};
        joueur["mise"]["argent parié"] = randrange(miseMin, miseMax+1);     
        # joueur["mise"] = {"argent parié":randrange(miseMin, miseMax+1)};
        
        # Choix du type de la mise du 'IA'
        typeMise = typeMiseIA[randrange(0, len(typeMiseIA))];
        joueur["mise"]["type"] = typeMise;
        
        # Si le joueur a misé sur ...
        # @ Nombre
        if (typeMise == "nombre") :
            # Le nombre que le joueur parie est tiré aléatoirement
            nombre = randrange(1, 37);
            joueur["mise"]["sur"] = nombre;
        # @ Couleur
        elif (typeMise == "couleur") :
            tmp = randrange(0, 2);
            if (tmp == 0) :
                joueur["mise"]["sur"] = "rouge";
            else :
                joueur["mise"]["sur"] = "noir";
        # @ Parité
        elif (typeMise == "parité") :
            tmp = randrange(0, 2);
            if (tmp == 0) :
                joueur["mise"]["sur"] = "pair";
            else :
                joueur["mise"]["sur"] = "impair";


# Se charge d'afficher toutes les mises que les joueurs ont fait
# (nom du joueur, sur quoi ils ont misé, argent parié)
def afficherMises(joueurs) :    
    for joueur in joueurs :
        # Si le joueur a misé sur ...
        # @ Nombre
        if (joueur["mise"]["type"] == "nombre") :
            print("{} a parié sur le nombre {} pour une somme de {} $".format(joueur["nom"], joueur["mise"]["sur"], joueur["mise"]["argent parié"]));
        # @ Couleur
        elif (joueur["mise"]["type"] == "couleur") :
            if (joueur["mise"]["sur"] == "noir") :
                print("{} a parié sur la couleur noire pour une somme de {} $".format(joueur["nom"], joueur["mise"]["argent parié"]));
            else :
                print("{} a parié sur la couleur rouge pour une somme de {} $".format(joueur["nom"], joueur["mise"]["argent parié"]));  
        # @ Parité
        elif (joueur["mise"]["type"] == "parité") :
            if (joueur["mise"]["sur"] == "pair") :
                print("{} a parié sur pair pour une somme de {} $".format(joueur["nom"], joueur["mise"]["argent parié"]));
            else :
                print("{} a parié sur impair pour une somme de {} $".format(joueur["nom"], joueur["mise"]["argent parié"]));
        
        attendre(0.5);


# Tire un nombre aléatoire de 0 à 36 et ensuite l'affiche
def tirerNombreRoulette() :
    # À chaque nombre de la roulette une couleur est associée
    couleursNombres = {1:"rouge", 2:"noir", 3:"rouge", 4:"noir", 5:"rouge",
    6:"noir", 7:"rouge", 8:"noir", 9:"rouge", 10:"noir", 11:"noir", 12:"rouge",
    13:"noir", 14:"rouge", 15:"noir", 16:"rouge", 17:"noir", 18:"rouge",
    19:"rouge", 20:"noir", 21:"rouge", 22:"noir", 23:"rouge", 24:"noir",
    25:"rouge", 26:"noir", 27:"rouge", 28:"noir", 29:"noir", 30:"rouge",
    31:"noir", 32:"rouge", 33:"noir", 34:"rouge", 35:"noir", 36:"rouge"};
    
    # Petite animation du genre "chargement en cours ..."
    print("La roulette tourne", end="");
    for i in range(3) :
        stdout.write('.')
        stdout.flush()
        attendre(0.7);    
   
    # Tire le nombre de la roulette alétoirement
    nombreRoulette = randrange(0, 37);
    if (nombreRoulette == 0) :
         print("\nLe numero {} est sorti ! Ahi !".format(nombreRoulette));
         return nombreRoulette;
    
    print("\nLe numero {} est sorti !".format(nombreRoulette), end=" ");
    couleur = couleursNombres[nombreRoulette];
    if (couleur == "noir") :
        print("Couleur : NOIRE");
    else :
        print("Couleur : ROUGE");
    
    return nombreRoulette;


# Calcule le score de chaque joueur
def calculerScore(joueurs, nombreRoulette) :
    # À chaque nombre de la roulette une couleur est associée
    couleursNombres = {1:"rouge", 2:"noir", 3:"rouge", 4:"noir", 5:"rouge",
    6:"noir", 7:"rouge", 8:"noir", 9:"rouge", 10:"noir", 11:"noir", 12:"rouge",
    13:"noir", 14:"rouge", 15:"noir", 16:"rouge", 17:"noir", 18:"rouge",
    19:"rouge", 20:"noir", 21:"rouge", 22:"noir", 23:"rouge", 24:"noir",
    25:"rouge", 26:"noir", 27:"rouge", 28:"noir", 29:"noir", 30:"rouge",
    31:"noir", 32:"rouge", 33:"noir", 34:"rouge", 35:"noir", 36:"rouge"};   
    
    # Cas 0 :
    if (nombreRoulette == 0) :
        print("Chaque joueur perd la moitié de sa mise !\n");
        attendre(0.5);
        
        for joueur in joueurs :
            mise = joueur["mise"];
            # Chaque joueur perd la moitié de l'argent qu'il avait parié
            joueur["portefeuille"] -= mise["argent parié"] // 2;
            print("{} perd {}$".format(joueur["nom"], mise["argent parié"] // 2));
            
            # Les joueurs qui doivent quitter la partie sont tirés
            # aléatoirement
            quittePartie = randrange(0, 2);
            if (quittePartie == 1) :
                joueur["perdu"] = True;
                            
            attendre(0.5);
        return;
        
    # Tous les autre cas
    for joueur in joueurs :
        mise = joueur["mise"];
        # Si le joueur a misé sur ...
        # @ Nombre
        if (mise["type"] == "nombre") :
            # Si le joueur a parié sur le bon nombre, il gagne 35 fois
            # sa mise + la mise initiale
            if (mise["sur"] == nombreRoulette) :
                joueur["portefeuille"] += mise["argent parié"] * 35;
                print("{}, qui a parié sur {}, gagne {}$x35 sa mise ! ({}$)".format(joueur["nom"], mise["sur"], mise["argent parié"], mise["argent parié"]*35));
            # Sinon il perd la somme d'argent parié
            else :
                joueur["portefeuille"] -= mise["argent parié"];
                joueur["perdu"] = True;
                print("{}, qui a parié sur {}, perd {}$".format(joueur["nom"], mise["sur"], mise["argent parié"]));             
        # @ Couleur
        elif (mise["type"] == "couleur") :
            # Si le joueur a parié sur le bon nombre, il gagne 1 fois
            # sa mise + la mise initiale
            if (mise["sur"] == couleursNombres[nombreRoulette]) :
                joueur["portefeuille"] += mise["argent parié"];
                print("{}, qui a parié sur {}, gagne {}$".format(joueur["nom"], mise["sur"], mise["argent parié"]));
            # Sinon il perd la somme d'argent parié
            else :
                joueur["portefeuille"] -= mise["argent parié"];
                joueur["perdu"] = True;
                print("{}, qui a parié sur {}, perd {}$".format(joueur["nom"], mise["sur"], mise["argent parié"]));
        # @ Parité
        elif (mise["type"] == "parité") :
            # Si le joueur a parié sur le bon nombre, il gagne 1 fois
            # sa mise + la mise initiale
            if (mise["sur"] == "pair" and nombreRoulette % 2 == 0) :
                joueur["portefeuille"] += mise["argent parié"];
                print("{}, qui a parié sur {}, gagne {}$".format(joueur["nom"], mise["sur"], mise["argent parié"]));
            # Sinon il perd la somme d'argent parié
            else :
                joueur["portefeuille"] -= mise["argent parié"];
                joueur["perdu"] = True;
                print("{}, qui a parié sur {}, perd {}$".format(joueur["nom"], mise["sur"], mise["argent parié"]));
        
        attendre(0.5);


# Affiche un classement des joueurs par rapport à l'argent qu'ils possèdent
def afficherClassement(joueurs) :
    # Change l'ordre des joueurs dans la liste selon l'argent qu'il
    # possèdent
    for i in range(len(joueurs)-1) :
        maximum = i;        
        for j in range(i+1, len(joueurs)) :
            if (joueurs[maximum]["portefeuille"] < joueurs[j]["portefeuille"]) :
                maximum = j;
        
        # Echange des positions
        tmp = joueurs[i];
        joueurs[i] = joueurs[maximum];
        joueurs[maximum] = tmp; 
    
    # Affichage du classement des joueurs (premier, deuxième etc.)
    print("- CLASSEMENT -\n");
    rang = 1;
    for joueur in joueurs :
        print("{}° {} avec {}$".format(rang, joueur["nom"], joueur["portefeuille"]));
        rang += 1;


# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :
    joueurs = [];
    jouer = True;
    while (jouer) :     
        # 1) Création des joueurs
        # Une liste contenant tous les joueurs sous forme
        # de dictionnaires est créée.
        creationJoueurs(joueurs);
        attendre(1);
        print("");      
                
        # 2) Tous le joueurs vont miser une somme d'argent soit sur la
        # valeur, couleur ou parité d'un nombre. Tout est stocké
        # ensuite dans le dictionnaire
        gestionMises(joueurs);          
        print("« Faites vos jeux »\n");
        attendre(1);        
        
        # 3) Les mises que les joueurs ont faites sont affichées
        afficherMises(joueurs);     
        attendre(0.7);
        print("\n« Rien ne va plus »\n");
        attendre(1);        
        
        # 4) Le nombre de la roulette est tiré aléatoirement, il servira
        # plus tard à calculer le score des joueurs
        #nbRoulette = tirerNombreRoulette();
        nbRoulette = tirerNombreRoulette();
        print("");
        attendre(0.7);
        
        # 5) Le score de chaque joueur est calculé et ensuite affiché
        calculerScore(joueurs, nbRoulette);
        
        print("");
        for i in range(4) :
            stdout.write('.')
            stdout.flush()
            attendre(0.7);
        
        effacerConsole();
        
        # 6) Un classement des joueurs est affiché avec leur score respectifs
        afficherClassement(joueurs);
        
        # 7) On demande à l'utilisateur s'il veut continuer la partie
        reponse = input("\n« Relancer la bille sur la roulette ? » (o/n) : ");
        if (reponse == 'o' or reponse == 'O') :
            jouer = True;
        else :
            jouer = False;
        
        effacerConsole();

