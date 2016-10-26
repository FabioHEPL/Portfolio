#!/usr/bin/python
#-*- coding: UTF-8 -*-

"""Module contenant les classes fondamentales à la création du jeu."""
import pygame

# ----------------------------------------------------------------------
# @ GAMEOBJECT
# ----------------------------------------------------------------------
class GameObject :
    """Classe de base dont tous les objets du jeu héritent
    
    Attributs de classe:
        allGameObjects  -- Liste contenant tous les gameobjects instanciés    

    """
    gameObjects = {};

    def init() :
        for i in range(Group.count()) :
            GameObject.gameObjects[Group.groupList[i]] = [];    
    
    def __init__(self, position=None, surface=None, group="Default") :
        """Crée une instance de la classe GameObject
        
        Paramètres:
            position -- la position de l'objet à l'écran [Vecteur2]
            surface  -- la surface représentant l'objet    
           
        """
        # Les données comme la position, la surface etc. du gameObject
        # son stockées dans des attributs pour l'affichage de l'objet
        # à l'écran
        self.position = position;
        self.rect = surface.get_rect();
        self.rect.center = (position.x, position.y);
        self.image = surface;
        
        # Á chaque fois qu'un gameObject est instancié, il est ajouté
        # à cette liste pour qu'il soit possible d'appeler la methode
        # update sur tous les gameObjects depuis la boucle principale
        GameObject.gameObjects[group].append(self);
        
        # Group and Layer
        self.group = group;
        

    def getRect(self) :
        """Renvoie la surface rectangulaire de l'objet."""
        return self.rect;

    def getPosition(self) :
        """Renvoie la position de l'objet à l'écran sous forme de coordonnées (x,y)."""
        return self.position;    

    def draw(self, surface) :
        """Dessine l'objet sur la surface donnée."""
        pygame.Surface.blit(surface, self.image, self.rect);
    
    def move(self, position) :
        """Permet de déplacer un objet à l'écran en lui envoyant des nouvelles cordonnées (x,y)."""
        self.position = position;
        self.rect.center = (position.x, position.y);

    def update(self) :
        """Methode principale de l'objet qui sera appelé à chaque frame"""
        return;
        
    def getGameObjects() :
        return GameObject.gameObjects;        
    
    def getGroup(self) :
        return self.group;    
    
    def onCollisionEnter(self, collider) :
        return;
        #print("{} collided with {}".format(self, collider));
    
    def destroy(self) :
        for i in range(len(GameObject.gameObjects[self.group])) :
            if (GameObject.gameObjects[self.group][i] == self) :
                del(GameObject.gameObjects[self.group][i]);
                break;

      
# ----------------------------------------------------------------------
# @ GROUP
# ----------------------------------------------------------------------
class Group :
    groupList = ["Default", "NoCollision", "Electron", "Positron", "Shell", "Background"];
    
    def getName(id) :
        return Group.groupList[id];
        
    def getID(name) :
        return Group.groupList.index(name);
        
    def count() :
        return len(Group.groupList);


# ----------------------------------------------------------------------
# @ CIRCLE
# ----------------------------------------------------------------------
class Circle(GameObject) :
    """Classe qui permet de gérér tout gameObject ayant une forme circulaire"""
    def __init__(self, position, radius, color, width=0, group="Default") :        
        # La surface sur laquelle le cercle est dessiné doit être rectangulaire,
        # la largeur et hauteur seront donc égales à 2x le rayon du cercle
        surface = pygame.Surface((radius * 2, radius * 2));

        GameObject.__init__(self, position, surface, group);
        
        # Définir la couleur transparente pour le fond du cercle
        transparentColor = ((255, 255, 254));
        self.image.fill(transparentColor);

        # Déssiner le cercle sur la surface vide avec un fond transparent
        pygame.draw.circle(surface, color, (radius, radius), radius, width);        
        #pygame.gfxdraw.circle(surface, radius, radius, radius, color);

        self.image.set_colorkey(transparentColor);
  

        self.radius = radius;

    def getRadius(self) :
        """Renvoie la rayon du cercle."""
        return self.radius;


# ----------------------------------------------------------------------
# @ PHYSICS
# ----------------------------------------------------------------------
class Physics :
    def checkCircleCollision(circleA, circleB) :
        """Vérifie si deux cercles sont en collision."""
        dx = circleA.getPosition().x - circleB.getPosition().x;
        dy = circleA.getPosition().y - circleB.getPosition().y;
        radiiSum = circleA.getRadius() + circleB.getRadius();

        if (dx**2 + dy**2 < radiiSum**2) :
            return True;
        else :
            return False;


# ----------------------------------------------------------------------
# @ INPUT
# ----------------------------------------------------------------------
class Input :
    """Classe qui capture les évenements clavier/souris
       
    Attributs de classe:
        keysPressed  -- Liste qui permet d'établir quelles touches clavier sont enfoncées
        keysDown -- Liste qui permet d'établir quelles touches clavier sont 'down'
        keysUp  -- Liste qui permet d'établir quelles touches clavier sont relachées
    
    """
    keysPressed = [];
    keysDown = [];
    keysUp = [];
    
    def isKeyPressed(keyCode) :
        """Renvoie true si la touche envoyé en paramètre est enfoncée, sinon False."""
        return Input.keysPressed[keyCode];

    def isKeyDown(keyCode) :
        """Renvoie true si la touche envoyé en paramètre est 'down', sinon False."""
        return Input.keysDown[keyCode];

    def isKeyUp(keyCode) :
        """Renvoie true si la touche envoyé en paramètre est relachée, sinon False."""
        return Input.keysUp[keyCode];

    def update(keysPressed) :
        """Methode principale de l'objet qui sera appelé à chaque frame pour établir
        quelles touches sont enfoncées, relachées etc.
        Attention: la classe Input n'est pas un gameObject."""

        for i in range(len(keysPressed)) :
            key = keysPressed[i];
            # Si la touche est enfoncée lors de ce frame
            if (key) :
                # Regarder si la touche était déjà enfoncée lors du frame précedent
                # pour établir si c'est un événement de type keydown
                if (not Input.isKeyPressed(i)) :
                    Input.keysDown[i] = True;
                else :
                    Input.keysDown[i] = False;

            # Si la touche n'est enfoncée lors de ce frame
            else :
                # Regarder si la touche était enfoncée lors du frame précedent 
                # pour établir si c'est un événement de type keyup ou pas
                if (Input.isKeyPressed(i)) :
                    Input.keysUp[i] = True;
                    Input.keysDown[i] = False;
                else :
                    Input.keysUp[i] = False;

            Input.keysPressed[i] = key;

    def init() :
        """Méthode d'initialisation de la classe Input"""
        for i in range(323) :
            Input.keysDown.append(False);
            Input.keysUp.append(False);
            Input.keysPressed.append(False);


# ----------------------------------------------------------------------
# @ TIME
# ----------------------------------------------------------------------
class Time :    
    _dt = 1;

    @property
    def deltaTime() :
        return _dt;

    @deltaTime.setter
    def deltaTime(time) :
        _dt = clock;
        

# ----------------------------------------------------------------------
# @ CONSTANTES
# ----------------------------------------------------------------------
# Collision Matrix : Matrice définissant les collisions dans le jeu
#                        B    S    P    E    NC   D
COLLISION_MATRIX =    [ [0,   1,   1,   1,   0,   1], # D
                        [0,   0,   0,   0,   0],      # NC
                        [0,   0,   1,   0],           # E 
                        [0,   1,   1],                # P
                        [0,   0],                     # S
                        [0] ];                        # B

# Draw Order : Définit l'ordre d'affichage des différents groupes
DRAW_ORDER = ["Background", "NoCollision", "Shell", "Electron", "Positron", "Default"];


# ----------------------------------------------------------------------
# @ INIT
# ----------------------------------------------------------------------
GameObject.init();

# Initialiser la classe Input
Input.init();

# Définir la valeur par défaut de la propriété deltaTime pour éviter
# d'éventuels bugs lors de son utilisation
Time.deltaTime = 1;


