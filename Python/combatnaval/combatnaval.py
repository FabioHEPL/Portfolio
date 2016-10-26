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

# On peut appeler la fonction "time.sleep" par "Wait()"
def Wait(secondes) :
    time.sleep(secondes);


# On peut appeler la fonction pour effacer ce qu'il y a écrit dans
# la console par "Clear()";
# La fonction se charge d'utiliser la bonne commande sur Windows et
# Linux
def Clear() :
    if (sys.platform == "win32") :
        os.system("cls");
    elif (sys.platform == "linux2") :
        os.system("reset");
        # sys.stderr.write("\x1b[2J\x1b[H")
        # print ('\n' * 100)



# ----------------------------------------------------------------------
# @ CLASSES
# ----------------------------------------------------------------------
class Terrain :
    # @) Constructeur
    def __init__(self, longueur, largeur) :        
        # @) Attribus
        # Liste bidimensionnelle qui représente la grille de jeu, cette
        # liste contiendra les positions des navires des joueurs et les
        # positions attaquées
        grille = [];
        self.longueur = longueur; # Longueur du terrain de jeu
        self.largeur = largeur; # Largeur du terrain de jeu
        
        # Positions occupées sur le terrain de jeu
        positionsOccupees = [];
        
        # Indices des colonnes du terrain de jeu
        indexColonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
        'X', 'Y', 'Z'];
        # Indices des lignes du terrain de jeu
        indexLignes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
        '22', '23', '24', '25', '26'];        
        
        # Se charge d'initialiser la grille de jeu, en créant une liste
        # bidimensionnelle avec un nombre de cases équivalent au produit
        # de la longueur et largeur données
        for i in range(longueur) :
            self.grille.append([]);
            for j in range(largeur) :
                self.grille[i].append(" ");

    
    # @) Méthodes
    def Afficher(self) :
        for i in range(-1, self.longueur) :
            if (i == -1) :
                print("\n   ", end="");
                for j in range(self.largeur) :
                    print("  {}".format(self.indexColonnes[j]), end="");
                print("\n")
            else :
                nombre = self.indexLignes[i];
                if (len(nombre) == 1) :
                    print("  {}".format(nombre), end="");
                else :
                    print(" {}".format(nombre), end="");
                
                for j in range(self.largeur) :
                    print("  {}".format(self.grille[i][j]), end="");
                print("\n")    
  
    
    def PlacerNavire(self, navire, coordonnee, orientation) :
        coordonnee.lettre = coordonnee.lettre.upper();
        orientation = orientation.upper();
        
        indexColonnes = self.indexColonnes[:largeur];
        indexLignes = self.indexLignes[:longueur];        
        
        # 1) Vérifier si la position du navire est bien une lettre (A -> J)
        #    suivie d'un nombre (0 ->  9) et que l'orientation est bien une
        #    lettre (soit H ou V)
        if  ((not coordonnee.lettre in indexColonnes)
        or  (not coordonnee.nombre in indexLignes)
        or  (orientation != 'H' and orientation != 'V')) :
            return PositionNavire.Inexistante;        
        
        # Calcule le numero de la colonne correspondante à la lettre donnée
        x = indexColonnes.index(coordonnee.lettre);
        # Calcule le numero de la ligne correspondante au nombre donnée
        y = indexLignes.index(coordonnee.nombre);       
        
        # 2) Vérifier que le navire ne se trouve pas le long d'un bord du 
        #    plateau de jeu
        if ((y == 0 or y == longueur-1) and orientation == 'H') or ((x == 0 or x == largeur-1) and orientation == 'V') :
            return PositionNavire.LongeBordsTerrain;        
        
        # 3) Vérifier que le navire ne touche pas les bords de la grille
        if (orientation == 'H') :
            if ((x + navire.taille) > largeur) :
                return PositionNavire.DepasseBordsTerrain;
        elif (orientation == 'V') :
            if ((y + navire.taille) > longueur) :
                return PositionNavire.DepasseBordsTerrain;        
        
        # 4) Vérifier que le navire ne touche pas d'autres navires
        for i in range(navire.taille) :        
            if (orientation == 'H') :
                if ((indexColonnes[x+i] + indexLignes[y]) in self.positionsOccupees) :           
                    return PositionNavire.ToucheAutresNavires;
            elif (orientation == 'V') :
                if ((indexColonnes[x] + indexLignes[y+i]) in self.positionsOccupees) :           
                   return PositionNavire.ToucheAutresNavires;        
        
        # 5) Si la position donnée respecte toutes les conditions
        #    précédentes, et donc résulte valide, alors placer le
        #    navire sur le terrain de jeu.
        if (orientation == 'H') :
            for i in range(-1, navire.taille+1) :            
                if (x+i > -1 and x+i < len(indexColonnes)) :                
                    for j in range(-1, 2) :
                        self.positionsOccupees.append(indexColonnes[x+i] + indexLignes[y+j]);
        
                if (i > -1 and i < navire.taille) :
                    self.grille[y][x+i] = 'x';
                    navire.positions.append(indexColonnes[x+i] + indexLignes[y]);  
                
        elif (orientation == 'V') :
            for i in range(-1, navire.taille+1) :           
                if (y+i > -1 and y+i < len(indexColonnes)) :                
                    for j in range(-1, 2) :
                        self.positionsOccupees.append(indexColonnes[x+j] + indexLignes[y+i]);
                
                if (i > -1 and i < navire.taille) :
                    self.grille[y+i][x] = 'x';
                    navire.positions.append(indexColonnes[x] + indexLignes[y+i]);            
        
        return PositionNavire.Valide;
    
    
class Joueur :
    lol = "kk.";
    
    def __init__(self, nom, couleur, terrain, terrainAdversaire, flotte=[]) :
        
        # @) Attribus
        self.nom = nom;
        self.couleur = couleur;
        self.terrain = terrain;
        self.terrainAdversaire = terrainAdversaire;
        self.flotte = flotte;
    
    def AttribuerFlotte(flotte) :
        self.flotte = flotte;

class Navire :
    
    positions = [];
    
    # Constructeur
    def __init__(self, nom, taille) :
        self.nom = nom;
        self.taille = taille;
        self.positions = [];


class Coordonnee :
    def __init__(self, lettre, nombre) :
        self.lettre = lettre;
        self.nombre = nombre;
    
    def Position(self) :
        return self.lettre + self.nombre;



# ----------------------------------------------------------------------
# @ ENUMS
# ----------------------------------------------------------------------
class PositionNavire() :
    (Inexistante,
    LongeBordsTerrain,
    DepasseBordsTerrain,
    ToucheAutresNavires,
    Valide) = range(5); 





# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
def CreationFlotte(joueur) :
    flotteDeBase = [["porte-avion", 5], ["croiseur", 4],
    ["destroyer", 3], ["sous-marin", 2]];
    
    flotte = [];    
    for navire in flotteDeBase :
        flotte.append(Navire(navire[0], navire[1]));
    
    joueur.flotte = flotte;


def PlacementNavires(joueur) :
    
    for navire in joueur.flotte :
        
        placementNavire = None;
        
        while (placementNavire != PositionNavire.Valide) :
            
            Clear();
            
            joueur.terrain.Afficher();
                        
            # Si le placement du navire a échoué, afficher un message
            # d'erreur.
            # Le contenu du message varie selon le type d'erreur qui
            # s'est produite lors du placement du navire
            if (placementNavire == PositionNavire.Inexistante) :
                print("La position donnée est inexistante.");
            elif (placementNavire == PositionNavire.LongeBordsTerrain) :
                print("Un navire ne peut pas longer les bords du terrain de jeu.");
            elif (placementNavire == PositionNavire.DepasseBordsTerrain) :
                print("Le navire dépasse les bords du terrain de jeu !");
            elif (placementNavire == PositionNavire.ToucheAutresNavires) :
                print("Un navire ne peut pas toucher d'autres navires !");
          
            # Demande à l'utilisateur les données nécessaires à
            # l'emplacement du navire
            print("Vas-y {}, places tes navires !".format(joueur.nom));
            print("Placement du {}".format(navire.nom, navire.taille));
            
            position = input("\tOù placez-vous votre {} [XY] : ".format(navire.nom));
            orientation = input("\tQuelle orientation pour votre {} [H/V] : ".format(navire.nom));      
            
            placementNavire = joueur.terrain.PlacerNavire(navire, Coordonnee(position[:1], position[1:]), orientation);
            
            
            

       

# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :    
    
    longueur = 10;
    largeur = 10;
    
    # Initialisation des deux joueurs
    joueur1 = Joueur("Fabio", "Jaune", Terrain(longueur, largeur), Terrain(longueur, largeur));
    joueur2 = Joueur("Julien", "Bleu", Terrain(longueur, largeur), Terrain(longueur, largeur));
   

    # Création flotte
    CreationFlotte(joueur1);
    CreationFlotte(joueur2);
           
    # Placement navires
    PlacementNavires(joueur1);
    PlacementNavires(joueur2);
    
    # Début bataille
    


