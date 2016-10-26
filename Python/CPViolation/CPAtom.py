#!/usr/bin/python
#-*- coding: UTF-8 -*-

from CPEngine import *
import math
from pygame.math import Vector2

# ----------------------------------------------------------------------
# @ ATOM
# ----------------------------------------------------------------------
class Atom() :
    def __init__(self, position, elementID) :
        """Crée une instance de la classe Atom
        
        Paramètres:
            position  -- la position de l'objet à l'écran [Vecteur2]
            elementID -- l'id de l'element dans la table périodique                
           
        """
        # Récupérer les informations nécéssaires sur l'atome
        element = PeriodicTable.GetElement(elementID);

        # Le nom de l'atome correspond au nome de l'élement de la table périodique
        self.name = element["name"];
        # Cordonnées indiquant le centre de l'atome
        self.position = position;
        # Liste contenant les couches électroniques de l'atome
        self.shells = [];
        # Rayon par défaut de la couche électronique la plus proche du noyau
        self.baseShellRadius = 300;
        # Écart entre chaque couche
        self.shellRadiusGap = 40;
        # Épaisseur des couches
        self.shellWidth = 6;
        
        # Création du noyau de l'atome
        self.nucleus = Nucleus(position, 20, element["symbol"], (40, 40, 40));
        
        #~ self.nucleus = Nucleus(position, pygame.image.load("./images/orb7.png").convert_alpha());

        atomShells = element["shells"];
        for i in range(atomShells) :
            shellRadius = self.baseShellRadius + (self.shellRadiusGap * i);

            # La dérnière couche électronique à être créée est la "couche externe" de l'atome
            if (i == atomShells-1) :
                shell = Shell(position, shellRadius, self.shellWidth, (40, 40, 40), True);
            else :
                shell = Shell(position, shellRadius, self.shellWidth, (40, 40, 40), False);

            # Création d'une liste contenant les éléctrons appartenant à la couche
            # électronique qui servira ensuite pour leur placement sur cette dernière
            electrons = [];
            electronsCount = element["electrons"][i];
            for i in range(electronsCount) :
                electrons.append(Electron(Vector2(0, 0), 7, (40, 40, 40)));

            # Disposer les éléctrons sur la couche
            shell.placeElectrons(electrons, 90);

            # Ajouter la couche qu'on vient de créer à la liste représenant
            # toutes les couche de l'atome
            self.shells.append(shell);

    def move(self, position) :
        """Permet de déplacer de déplacer l'atome à l'écran en lui envoyant des nouvelles cordonnées (x,y)."""
        self.position = position;
        
        self.nucleus.move(position);
                
        for i in range(len(self.shells)) :
            self.shells[i].move(position);


# ----------------------------------------------------------------------
# @ NUCLEUS
# ----------------------------------------------------------------------
class Nucleus(Circle) :
    def __init__(self, position, radius, symbol, color) :
        Circle.__init__(self, position, radius, color, 0, "NoCollision");        
        
        self.symbol = symbol;


# ----------------------------------------------------------------------
# @ SHELL
# ----------------------------------------------------------------------
class Shell(Circle) :
    def __init__(self, position, radius, width, color, isValence=False) :
        """Crée une instance de la classe Shell
        
        Paramètres:
            position  -- la position de l'objet à l'écran [Vecteur2]
            radius    -- rayon de la couche éléctronique
            width     -- épaisseur de la couche éléctronique          
            color     -- couleur de la couche éléctronique
            isValence -- détermine si la couche éléctronique est une couche externe
           
        """
        # Vu que la couche éléctronique a une forme circulaire, elle est d'abord instanciée
        # en tant qu'objet 'Circle'
        Circle.__init__(self, position, radius, color, width, "Shell");       
        
        self.electrons = []
        self.isValence = isValence;
        self.width = width;

        # Vitesse à laquelle la couche éléctronique tourne
        self.speed = 150 / (2 * math.pi * self.radius);

        # L'angle de référence de la couche éléctronique utilisé principalement pour
        # y disposer les éléctrons
        self.angle = 0;        

        if (isValence) :
             self.image.set_alpha(125);
        else :
            self.image.set_alpha(70);

    def placeElectrons(self, electrons, offset) :
        """Place un ou plusieurs éléctrons sur une couche éléctronique."""
        # Les éléctrons qui sont placés appartiennent maintenant à la couche éléctronique
        self.electrons = electrons;
                
        # Calcule l'angle d'espacement entre les éléctrons
        self.angle -= offset;       
        offset = math.pi * (self.angle) / 180;        
        spanAngle = 2*math.pi / len(self.electrons);

        # Placé les éléctrons sur la couche éléctronique à égale distance entre eux
        shellCenter = self.radius - (self.width / 2);
        for i in range(len(electrons)) :
            x = self.rect.centerx + shellCenter * math.cos(spanAngle*i - offset);
            y = self.rect.centery + shellCenter * math.sin(spanAngle*i - offset);

            electrons[i].move(Vector2(x, y));

    def rotate(self, degrees) :
        """Fait tourner la couche éléctronique de 'x' degrés (x = 'degrees')"""
        self.placeElectrons(self.electrons, degrees);

    def update(self) :
        """Methode principale de l'objet qui sera appelé à chaque frame"""
        
        if (self.isValence) :
            # Si on appuye sur la flèche droite, faire tourner la couche externe
            # dans le sens horloger
            if (Input.isKeyPressed(pygame.K_RIGHT)) :
                self.rotate(self.speed * Time.deltaTime);                
            # Si on appuye sur la flèche gauche, faire tourner la couche externe
            # dans le sens anti-horloger
            elif (Input.isKeyPressed(pygame.K_LEFT)) :
                self.rotate(-self.speed * Time.deltaTime);


# ----------------------------------------------------------------------
# @ ELECTRON
# ----------------------------------------------------------------------
class Electron(Circle) :
    def __init__(self, position, radius, color) :
        Circle.__init__(self, position, radius, color, 0, "Electron");



# ----------------------------------------------------------------------
# @ POSITRON
# ----------------------------------------------------------------------
class Positron(Circle) :
    def __init__(self, position, radius, color) :
        Circle.__init__(self, position, radius, color, 0, "Positron");
        
    def onCollisionEnter(self, collider) :
        if (collider.getGroup() == "Shell") :
            self.destroy();
        
        
# ----------------------------------------------------------------------
# @ PARTICLE SPAWNER
# ----------------------------------------------------------------------
class ParticleSpawner(GameObject) :
    def __init__(self, position, surface) :
        GameObject.__init__(self, position, surface, "NoCollision");
        
        self.positrons = [];
        
        self.positrons.append(Positron(self.position, 5, (80, 70, 255)));
        
    def update(self) :
        for positron in self.positrons : 
            x = (positron.getPosition().x + 1) * (Time.deltaTime / 10);
            y = (positron.getPosition().y + 1) * (Time.deltaTime / 10);
            print(x, y);
            positron.move(Vector2(x, y));    


# ----------------------------------------------------------------------
# @ BACKGROUND
# ----------------------------------------------------------------------
class Background(GameObject) :
    def __init__(self, position, surface) :
        GameObject.__init__(self, position, surface, "Background");
        

# ----------------------------------------------------------------------
# @ PERIODIC TABLE
# ----------------------------------------------------------------------
class PeriodicTable :
    # Dictionnaire contenant toutes les informations sur les atomes
    table = {};

    # Liste des éléments dans la table périodique (Enum)
    
    # Renvoie toutes les informations nécessaire sur l'atome demandé
    def GetElement(atomType) :
        return PeriodicTable.table[atomType];
    
    # Initialise la table
    def init() :
        fileName = "periodic_table.txt";
        fieldNames = ["name", "symbol", "atomicNumber", "shells", "electrons"];

        file = open(fileName);

        for line in file :
            # Si la ligne est un commentaire, passer à la suivante
            if (line[0] == '/' and line[1] == '/') :
                continue;

            data = line.split('|');

            id = int(data[2]);
            PeriodicTable.table[id] = {};

            for field, fieldName in zip(data, fieldNames) :
                field = field.strip();
                
                if (fieldName == "electrons") :
                    electronsPerShell = field.split(' ');
                    
                    for i in range(len(electronsPerShell)) :
                        electronsPerShell[i] = int(electronsPerShell[i]);

                    field = electronsPerShell;

                elif (fieldName == "atomicNumber" or fieldName == "shells") :
                    field = int(field);

                PeriodicTable.table[id][fieldName] = field;




# ---------------------------------------------------------------------
# @ ATOM LIST
# ----------------------------------------------------------------------
class AtomList :
    Hydrogen = 1; Helium = 2; Lithium = 3; Beryllium = 4; Boron = 5;
    Carbon = 6; Aluminium = 7;


# ----------------------------------------------------------------------
# @ INIT
# ----------------------------------------------------------------------
PeriodicTable.init();