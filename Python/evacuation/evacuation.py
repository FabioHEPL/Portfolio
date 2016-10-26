#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       combatnaval-boucfab.py
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc55>
#


# ----------------------------------------------------------------------
# @ FONCTIONS UTILES
# ----------------------------------------------------------------------
import os
import time
import sys
import random


# On peut appeler la fonction "time.sleep" par "Wait()"
def attendre(secondes) :
    time.sleep(secondes);


# On peut appeler la fonction pour effacer la console par "Clear()"
# La fonction se charge d'utiliser la bonne commande sur Windows et
# Linux
def effacerConsole() :
    if (sys.platform == "win32") :
        os.system("cls");
    elif (sys.platform == "linux2") :
        os.system("clear");


# ----------------------------------------------------------------------
# @ CLASSES
# ----------------------------------------------------------------------
class Piece :
    def __init__(self, largeur, longueur) :
        # Liste bidimensionnelle qui représente la pièce, cette
        # liste contiendra les positions des differents objets/entités
        # (murs, obstacles, humains ...)
        self.grille = [];
        self.largeur = largeur;   # largeur de la pièce 
        self.longueur = longueur; # longueur de la pièce       
        
        
        # Initialisation de la grille (longueur x largeur)
        for i in range(longueur) :
            self.grille.append([]);
            for j in range(largeur) :
                self.grille[i].append(Vide(1, 1));
    
    
    # Représente la pièce à l'écran en 2D, sous forme de grille
    def afficher(self) :
        for i in range(self.longueur) :
            for j in range(self.largeur) :
                if (j+1 != self.largeur) :
                    print(self.grille[i][j].representation, end=" ");
                else :
                    # Si c'est le dernier élément affiché d'une ligne
                    # ne pas mettre d'espaces après
                    print(self.grille[i][j].representation, end="");
            
            print("");
    
    
    # Renvoie les coordonnées des coins de la pièce
    
    # Coin en haut à gauche
    def coinHautGauche(self) :
        return Coordonnee(0, 0);
    
    # Coin en haut à droite
    def coinHautDroite(self) :
        return Coordonnee(self.largeur-1, 0);
    
    # Coin en bas à gauche
    def coinBasGauche(self) :
        return Coordonnee(0, self.longueur-1);
    
    # Coin en bas à droite
    def coinBasDroite(self) :
        return Coordonnee(self.largeur-1, self.longueur-1);
    
    
    # Méthode qui permet de placer un objet dans la pièce
    # La méthode se charge de vérifier si c'est possible de placer
    # l'objet dans la pièce
    # Objet : l'objet qu'il faut placer (de type 'Entité') largeur longueur
    # Position : position de l'objet dans la pièce ('origine' pour 
    # les objets qui occupent plus qu'une case dans la grille), nécessaire
    # pour savoir où positionner l'objet
    def placerObjet(self, objet, position) :
        y = position.y;
        x = position.x;
        
        for i in range(objet.longueur) :
            for j in range(objet.largeur) :
                self.grille[y+i][x+j] = objet; 
 
 
                
class Objet :
    def __init__(self, largeur, longueur) :
        self.largeur = largeur;   # largeur de la grille  
        self.longueur = longueur; # longueur de la grille        



class Humain(Objet) :
    def __init__(self, largeur, longueur) :
        Objet.__init__(self, largeur, longueur);
        self.representation = 'H';
        self.collision = True;


class Porte(Objet) :
    def __init__(self, largeur, longueur) :
        Objet.__init__(self, largeur, longueur);
        self.representation = 'P';
        self.collision = False;
        
    
class Obstacle(Objet) :
    def __init__(self, largeur, longueur) :
        Objet.__init__(self, largeur, longueur);
        self.representation = 'O';
        self.collision = True;



class Vide(Objet) :
    def __init__(self, largeur, longueur) :
        Objet.__init__(self, largeur, longueur);
        self.representation = ' ';
        self.collision = False;


class Mur(Objet) :
    def __init__(self, largeur, longueur) :
        Objet.__init__(self, largeur, longueur);
        self.representation = 'X';
        self.collision = True;
        self.possedePorte = False;
    
class Coordonnee :
    def __init__(self, x, y) :
        self.x = x;
        self.y = y;


# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
def placerMurs(piece) :
    # Création des murs
    # Mur de gauche et droite couvrent toute la longueur de la pièce
    murGauche = Mur(1, piece.longueur);
    murDroite = Mur(1, piece.longueur);
    
    # Mur de haut et bas se trouvent entre les mur qui couvrent la longueur
    # sur les côtés haut et bas
    murHaut = Mur(piece.largeur-2, 1);
    murBas = Mur(piece.largeur-2, 1);    
    
    # Placement des murs
    piece.placerObjet(murGauche, piece.coinHautGauche());
    piece.placerObjet(murDroite, piece.coinHautDroite());    
    
    posMurHaut = Coordonnee(piece.coinHautGauche().x+1, piece.coinHautGauche().y);
    piece.placerObjet(murHaut, posMurHaut);
    
    posMurBas = Coordonnee(piece.coinBasGauche().x+1, piece.coinBasGauche().y);
    piece.placerObjet(murBas, posMurBas);


def placerPortes(piece) :
    pass;


def placerObstacles(piece) :
    pass;

    
def placerHumains(piece) :
    pass;

# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :
    # @ Création de la pièce
    piece = Piece(20, 20);
    
    # ------------------------------------------------------------------
    # 1. Placer les murs sur les côtés 
    # ------------------------------------------------------------------
    # Création des murs
    # Mur de gauche et droite couvrent toute la longueur de la pièce
    murGauche = Mur(1, piece.longueur);
    murDroite = Mur(1, piece.longueur);
    
    # Mur de haut et bas se trouvent entre les mur qui couvrent la longueur
    # sur les côtés haut et bas
    murHaut = Mur(piece.largeur-2, 1);
    murBas = Mur(piece.largeur-2, 1);    
    
    # Placement des murs
    piece.placerObjet(murGauche, piece.coinHautGauche());
    piece.placerObjet(murDroite, piece.coinHautDroite());    
    
    posMurHaut = Coordonnee(piece.coinHautGauche().x+1, piece.coinHautGauche().y);
    piece.placerObjet(murHaut, posMurHaut);
    
    posMurBas = Coordonnee(piece.coinBasGauche().x+1, piece.coinBasGauche().y);
    piece.placerObjet(murBas, posMurBas);
    
    
    # ------------------------------------------------------------------
    # 2. Placer les portes
    # ------------------------------------------------------------------
    # Le nombre de portes est tiré aléatoirement (entre 2 et 4);
    nombrePortes = random.randrange(2, 5);
    murs = [murGauche, murDroite, murHaut, murBas];
    random.shuffle(murs);
    
    i = 0;
    while (i < nombrePortes) :
        # Placement de la porte dans le mur
        
        
        
        i += 1;
    
    # ------------------------------------------------------------------
    # 3. Placer les obstacles
    # ------------------------------------------------------------------
    
    
    # ------------------------------------------------------------------
    # # 4. Placer les humains
    # ------------------------------------------------------------------

    

    
    
    
    piece.afficher();
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
