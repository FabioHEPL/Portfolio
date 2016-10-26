#!/usr/bin/python
#-*- coding: UTF-8 -*-

import pygame
from CPModules import *

# ----------------------------------------------------------------------
# @ INITIALISATION
# ----------------------------------------------------------------------
pygame.init();

# Définit la largeur et la hauteur de l'écran
SCREEN_WIDTH = 1280;
SCREEN_HEIGHT = 720;

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
clock = pygame.time.Clock();
goGroups = GameObject.getGameObjects();


# ----------------------------------------------------------------------
# @ CRÉATION DES OBJETS
# ----------------------------------------------------------------------
back_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT));
back_surface.fill((153, 255, 255));
Background(Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), back_surface);

ParticleSpawner(Vector2(0, 0), pygame.Surface((0, 0)));

#positronTest = Positron(Vector2(400, 400), 10, (30, 200, 20));

k = Atom(Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), AtomList.Hydrogen);


positronTestM = Positron(Vector2(-400, 400), 10, (30, 200, 20))

# ----------------------------------------------------------------------
# @ BOUCLE PRINCIPALE
# ----------------------------------------------------------------------
running = True;
while (running) :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False;
       
    # 1) Méttre à jour la classe Input pour gèrer le touches
    Input.update(pygame.key.get_pressed());  
     
    # 2) Vérifier les collision pour chaque gameObject
    for i in range(len(COLLISION_MATRIX)) :        
        for j in range(len(COLLISION_MATRIX[i])) :            
            if (COLLISION_MATRIX[i][j] == True) :
                
                for group in goGroups :
                    for go in goGroups[Group.getName(i)] :                                        
                        for otherGO in goGroups[Group.getName( (Group.count()-1) - j )] :                      
                            if (go == otherGO) :
                                continue;
                        
                        if (Physics.checkCircleCollision(go, otherGO)) :
                            go.onCollisionEnter(otherGO);
                            otherGO.onCollisionEnter(go);    
        
    # 3) Appel de la fonction update de chaque gameObject
    for group in goGroups :
        for i in range(len(goGroups[group])) :
            goGroups[group][i].update();
    
    # 4) Affichage des gameObjects en utilisant le "draw order"
    for group in DRAW_ORDER :
        for i in range(len(goGroups[group])) :
            goGroups[group][i].draw(display); 
    
    # 5) Mise à jour du deltaTime
    Time.deltaTime = clock.tick(120);    
    
    print(clock.get_fps());

    # 6) Rafraichir l'écran
    pygame.display.flip();
    


