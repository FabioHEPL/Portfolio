#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       blackjack_fct-boucfab.py
#       version 1.0
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc55>
#


# ----------------------------------------------------------------------
# @ FONCTIONS UTILES
# ----------------------------------------------------------------------
from random import randrange
from random import shuffle
from sys import platform
from time import sleep
from os import system 

# On peut appeler la fonction "time.sleep" par "attendre()"
def attendre(secondes) :
    sleep(secondes);


# On peut appeler la fonction pour effacer ce qu'il y a écrit dans
# la console par "effacerConsole()";
# La fonction se charge d'utiliser la bonne commande sur Windows et
# Linux
def effacerConsole() :
    if (platform == "win32") :
        system("cls");
    elif (platform == "linux2") :
        print("\033c");


# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
# Création du jeu de cartes
# Chaque carte est representée par un tuple, où le premier élément
# contient la valeur de la carte et le deuxième sa famille
# (l'as est representé par le nombre 14)
def jeuDeCartes(nb) :
    # Liste contenant toutes les cartes
    jeu = [];
    
    valeurCarte = 2;
    while (len(jeu) < nb) :
        familleCarte = 1;
        while (familleCarte <= 4) :
            # valeurCarte = la valeur de la carte (de 2 à 14)
            # familleCarte = la famille de la carte (cœur(1), carreau (2),
            # trèfle (3) et pique (4))
            jeu.append((valeurCarte, familleCarte));
            familleCarte += 1;        
        valeurCarte += 1;
    
    return jeu;


# Mélange les cartes et renvoie le jeu mélangé
def melangerCartes(tas) :
    # À chaque itération une carte est choisie aléatoirement dans le tas
    # et ensuite sa position est échangée avec la position de la carte
    # à l'index de la valeur de i (variable qui parcourt la boucle)
    for i in range(len(tas)) :
        elementAleatoire = randrange(i, len(tas));
        
        # Echange de position entre l'élement choisi aléatoirement et
        # celui à l'index 'i'
        tmp = tas[i];
        tas[i] = tas[elementAleatoire];
        tas[elementAleatoire] = tmp;

    return tas;


# Renvoie la valeur de la carte dans le jeu blackjack envoyée
# comme paramètre
def valeurCarte(c, ace=True) :
    valeur = c[0];
    
    # Si la carte est un As ...
    if (valeur == 14) :
        # Si ace est true renvoyer 11
        if (ace) :
            return 11;
        # Si ace est False retourner 1
        else :
            return 1
    # Si la carte est une buche renvoyer 10
    elif (valeur > 10) :
        return 10;
    # Sinon renvoyer la valeur de base de la carte
    else :
        return valeur;


# Renvoie True si la main est un BlackJack sinon renvoie False
def blackjack(main) :
    # Si la main n'est pas composée de 2 carte le joueur n'aura pas
    # de blackjack
    if (len(main) != 2) :
        return False;
    
    somme = valeurMain(main, True);
    
    if (somme == 21) :
        return True;
    else :
        return False;


# Renvoie la première carte du tas qui est effacée au même temps de
# la liste
def donnerCarte(tas) :
    carte = tas[0];
    del(tas[0]);
    
    return carte;


# Renvoie la valeur en points de la main, deux versions :
# 1) Si le joueur n'est pas humain, la valeur des As sera calculée par
#    le programme
# 2) Si le joueur est humain, le joueur pourra choisir la valeur des As
def valeurMain(main, IA) :
    # Si le joueur est humain ...
    if (IA) :
        # Variable qui stocke la somme des valeurs des différentes cartes
        # dans la main, et donc la valeur de la main
        somme = 0;
        # Si asMax vaut True, l'as vaudra 11 sinon 1
        asMax = True; 
        
        for carte in main :
            # Si la carte n'est pas un as ...
            if (valeurCarte(carte, True) != 11) :                
                somme += valeurCarte(carte);
            
        for carte in main :
            # Si la carte est un as ...
            if (valeurCarte(carte, True) == 11) :
                if (asMax and (somme + valeurCarte(carte, True) < 22) ) :
                    somme += valeurCarte(carte, True);
                    asMax = False;
                else :                    
                    somme += valeurCarte(carte, False);
    
    # Si le joueur n'est pas humain ...
    else :
        # Stocke le nombre d'As dans la main du joueur
        nbAs = 0;
        for carte in main :
            # Si la carte n'est pas un as ...
            if (valeurCarte(carte, True) != 11) :                
                somme += valeurCarte(carte);
            # Sinon ...
            else :
                nbAs += 1;
        
        print(nbAs);
        input();
        
        if (nbAs == 1) :
            print("Votre main vaut {} sans compter le seul As dont vous disposez.".format(somme));
            reponse = input("Quelle valeur voulez-vous donner à votre As (1 ou 11) ? ");
            
           
        elif (nbAs > 1) :
            print("Votre main vaut {} sans compter les {} As dont vous disposez.".format(somme, nbAs));
            
            for i in range(nbAs) :
                reponse = input("Quelle valeur voulez-vous donner à votre {}° As (1 ou 11) ? ".format(i+1));
                somme += int(reponse);
        
    return somme;


# Renvoie -1 le joueur saute, 0 s'il passe ou 1 s'il continue
def sauteOuPasse(main, IA) :
    # Si le joueur est humain ...
    if (IA) :
        # Pour l'IA, passer au joueur suivant si le score est compris
        # entre 18 et 21
        if (valeurMain(main, True) > 21) :
            return -1;
        elif (valeurMain(main, True) >= 18 and valeurMain(main, True) <= 21) :
            return 0;
        else :
            return 1;
    
    # Si le joueur n'est pas humain ...
    else :
        # Si la valeur minimale de la main dépasse 21 le joueur saute
        if (valeurMainMin(main) > 21) :
            print("La valeur minimale de votre main dépasse 21, vous sautez !");
            attendre(1.5);
            return -1;        
        
        
        reponse = "";
        while (reponse != 'p' and reponse != 'c') :       
            # Affiche les différentes cartes de la main du joueur
            # pour qu'il puisse choisir si passer ou continuer
            afficherMain(main);
            
            print("\nValeur minimale de la main : {}".format(valeurMainMin(main)));      
        
            reponse = input("\nVoulez-vous passer ou continuer [p/c] ? ");
            if (reponse == 'p') :
                return 0;
            else :
                return 1;


# Renvoie la valeur minimale de la main (les As valent 1)
def valeurMainMin(main) :
    somme = 0;
    for carte in main :
        valeur = valeurCarte(carte, False);
        somme += valeur;
    
    return somme;


# Affiche les différentes cartes et leurs valeurs eventuelles
def afficherMain(main) :
    print("Votre main est composée de :");
    
    for carte in main :
        valeur = valeurCarte(carte, True);        
        
        if (valeur == 11) :
            print("- Un As (1 ou 11)");
        else :
            print("- Un {} ({})".format(valeur, valeur));
            

# Affiche le classement des joueurs
def afficherClassement(joueurs) :
    print(" - CLASSEMENT - \n");
    
    for i in range(len(joueurs)-1) :
        maximum = i;
        for j in range(i+1, len(joueurs)) :
            if ((valeurMain(joueurs[maximum]["main"], True) > 21 or
                valeurMain(joueurs[j]["main"], True) > valeurMain(joueurs[maximum]["main"], True))
                and valeurMain(joueurs[j]["main"], True) <= 21) :
                    maximum = j;
        
        # Echange des positions
        tmp = joueurs[i];
        joueurs[i] = joueurs[maximum];
        joueurs[maximum] = tmp;
        
    
    rang = 1;
    for i in range(len(joueurs)) :
        if (valeurMain(joueurs[i]["main"], True) > 21) :
            print("{}. xx - {}".format(rang, joueurs[i]["nom"]));
        else :
            if (blackjack(joueurs[i]["main"])) :
                print("{}. {} - {} (Blackjack)".format(rang, valeurMain(joueurs[i]["main"], True), joueurs[i]["nom"]));
            else :
                print("{}. {} - {}".format(rang, valeurMain(joueurs[i]["main"], True), joueurs[i]["nom"]));
        
        if (i != len(joueurs)-1) :
            if (valeurMain(joueurs[i]["main"], True) != valeurMain(joueurs[i+1]["main"], True)) :
                rang += 1;


if __name__ == "__main__" :
    # Noms disponibles pour les joueurs
    nomsJoueurs = ["Paul", "Jean-Yves", "Julien", "François", "Marco",
                   "Sasha", "Cyril", "Pauline", "Renaud", "Pierre",
                   "Jules", "Yannou", "Jerôme", "Fanny", "Guillaume",
                   "Fabio", "Jimmy"];
            
    # 1) Création des joueurs
    maxJoueurs = 1;
    nbJoueursHumains = 4;
    
    # Liste principale contenant toutes les données des joueurs
    joueurs = [];
    
    # La liste contenant les noms des joueurs est mélangée pour ne pas
    # que les joueurs aient toujours les mêmes noms
    shuffle(nomsJoueurs);
    
    for i in range(maxJoueurs) :
        # Dictionnaire qui représente tous le joueur et contenant
        # toutes ses propriétés (nom, main, ...)
        attribus = {};

        attribus["main"] = [];
        
        if (nbJoueursHumains != 0) :
            attribus["IA"] = False;
            
            
            #~ nom = input("Inserez votre nom : ");
            #~ attribus["nom"] = nom;
            
            nom = "test{}".format(nbJoueursHumains);            
            attribus["nom"] = nom;
            attribus["main"] = [(14, 1), (14, 2), (14, 2)];
            
            nbJoueursHumains -= 1;
        else :
            attribus["IA"] = True;
            attribus["nom"] = nomsJoueurs[i];
        
        joueurs.append(attribus);
    
    effacerConsole();
    
    
    # 2) Création du jeu de cartes
    jeu = jeuDeCartes(52);
    
    
    # 3) Le jeu de cartes est mélangé
    jeu = melangerCartes(jeu);
    
    
    # 4) Début du jeu
    for joueur in joueurs :        
        if (joueur["IA"] == False) :
            print("{} c'est votre tour !".format(joueur["nom"]));
            attendre(1.5);

        jouer = True;
        while (jouer) :
            # Tant que jouer est égal à True, on distribue une carte
            # au joueur qui joue
            joueur["main"].append(donnerCarte(jeu));
            
            # Si le joueur n'est pas humain ...
            if (joueur["IA"] == True) :
                reponse = sauteOuPasse(joueur["main"], True);
            else :
                reponse = sauteOuPasse(joueur["main"], False);              
            
            if (reponse == -1 or reponse == 0) :                      
                break;
            
            effacerConsole();
    
    

    
    # 5) Affichage du classement des joueurs
    afficherClassement(joueurs)
    
    print("\n");


   
