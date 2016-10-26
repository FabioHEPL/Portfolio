# -*- coding: utf-8 -*-
# BOUCHÉ Fabio 6TB
# Domino-boucfab.py – date 14.11.2013

from random import randrange, shuffle
import time
import os
import sys

# ----------------------------------------------------------------------
# @ CLASSES
# ----------------------------------------------------------------------
class Domino :
    def __init__(self, a, b) :
        self.faceA = a;
        self.faceB = b;
        self.owner = None;

    # Représente le domino sous forme de chaîne : [A·B]
    def __str__(self) :
        return "[{}·{}]".format(self.faceA, self.faceB);
    
    # Renvoie la valeur de la face A du domino (celle à gauche)
    def getFaceA(self) :
        return self.faceA;

    # Renvoie la valeur de la face A du domino (celle à droite)
    def getFaceB(self) :
        return self.faceB;

    # Inverse les valeurs du domino
    def invert(self) :
        self.faceA, self.faceB = self.faceB, self.faceA;
    
    # Renvoie la valeur totale du domino, donnée par la somme 
    # de la valeur des deux faces
    def getValue(self) :
        return self.faceA + self.faceB;

    # Renvoie une référence vers le joueur qui possède le domino
    def getOwner(self) :
        return self.owner;

    # Permet d'attribuer le domino à un joueur
    def setOwner(self, owner) :
        self.owner = owner;
        
    # Détermine si les deux faces du domino ont la même valeur
    def isDouble(self) :
        if (self.faceA == self.faceB) :
            return True;
        else :
            return False;


class Player :
    count = 1;

    def __init__(self, name) :
        self.hand = [];
        self.name = name;
        self.play = True;
        Player.count += 1;

    # Renvoie le nom du joueur
    def getName(self) :
        return self.name;

    # Determine si le joueur peut jouer ou pas
    @property
    def canPlay(self) :
        return self.play; 
    @canPlay.setter
    def canPlay(self, value) :
        self.play = value;

    # Ajoute un domino à la main du joueur
    def addDomino(self, domino) :
        domino.setOwner(self);
        self.hand.append(domino);

    # Efface un domino de la main du joueur
    def removeDomino(self, domino) :
        pos = self.hand.index(domino);
        self.hand[pos].setOwner(None);
        del(self.hand[pos]);

    # Renvoie la main du joueur
    def getHand(self) :
        return self.hand;
    
    # Renvoie 'True' si le joueur n'a plus de dominos en main
    def hasEmptyHand(self) :
        if (len(self.hand) == 0) :
            return True;
        else :
            return False;


class GameTable :
    def __init__(self) :
        self.game = [];

        # Création de la pioche
        self.stock = [];
        for i in range(7) :
            for j in range(i, 7) :
                self.stock.append(Domino(i, j));

    # Renvoie True s'il n'y a plus de dominos dans la pioche
    def isStockEmpty(self) :
        if (len(self.stock) == 0) :
            return True;
        else :
            return False;

    # Renvoie la liste des dominos dans le jeu
    def getGame(self) :
        return self.game;

    # Renvoie la valeur de l'extremité gauche du jeu
    def getFirst(self) :
        if (len(self.game) == 0) :
            return None;
        else :
            return self.game[0].getFaceA();

    # Renvoie la valeur de l'extremité droite du jeu
    def getLast(self) :
        if (len(self.game) == 0) :
            return None;
        else :
            return self.game[len(self.game)-1].getFaceB();

    # Renvoie une référence vers le domino pioché dans le tas
    def pickupDomino(self, remove=True) :
        # Si la pioche est vide renvoyer None
        if (len(self.stock) == 0) :
            return None;

        # On choisi un domino aléatoirement dans le tas
        randomDomino = randrange(0, len(self.stock));
        
        if (not remove) :
            return self.stock[randomDomino];

        # Pour garder une référence vers le domino aléatoire, avant
        # de l'effacer du tas il est stocké dans une variable temporaire
        tmp = self.stock[randomDomino];
        del(self.stock[randomDomino]);
        
        return tmp;

    def placeDomino(self, domino) :
        # Si la liste du jeu est vide, cela signifie que personne n'a toujours
        # placé de dominos en jeu
        if (len(self.game) == 0) :
            self.game.append(domino);
        elif (domino.getFaceA() == self.getFirst()) :
            domino.invert();
            self.game.insert(0, domino);
        elif (domino.getFaceB() == self.getFirst()) :
            self.game.insert(0, domino);
        elif (domino.getFaceA() == self.getLast()) :
            self.game.append(domino);
        elif (domino.getFaceB() == self.getLast()) :
            domino.invert();
            self.game.append(domino);
        else :
            return False;
        
        return True;


# ----------------------------------------------------------------------
# @ FONCTIONS
# ----------------------------------------------------------------------
# Renvoie les dominos doubles dans une liste de dominos
def getDoubleDominoes(dominoList) :
	doubleDominoes = [];

	# Vérifie pour chaque domino dans la liste s'il est double,
	# si c'est le cas, il l'ajoute dans la liste des dominos doubles
	for i in range(len(dominoList)) :
		if (dominoList[i].isDouble()) :
			doubleDominoes.append(dominoList[i]);

	return doubleDominoes;


# Renvoie le plus grand domino dans une liste de dominos
def getMaxDomino(dominoList) :
	maxDomino = 0;

	# Récupère l'index du domino plus grand dans la liste
	for i in range(len(dominoList)) :
		if (dominoList[maxDomino].getValue() < dominoList[i].getValue()) :
			maxDomino = i;

	return dominoList[maxDomino];


# Compte le nombre de joueurs qui savent jouer un domino
def countPlayersAbleToPlay(players) :
    count = 0;
    for i in range(len(players)) :
        if (players[i].canPlay) :
            count += 1;

    return count;


# Affiche le jeu
def printGame(game) :
    for i in range(len(game)) :
        if (i == len(game)-1) :
            print(game[i], end="");
        else :
            print(game[i], end=" ");


# Efface ce qu'il y a écrit dans la console
def clearConsole() :
    if (sys.platform == "win32") :
        os.system("cls");
    elif (sys.platform == "linux2") :
        os.system("clear");


# Renvoie la valeur de la main du joueur
def getHandValue(playerHand) :
    total = 0;
    for i in range(len(playerHand)) :
        total += playerHand[i].getValue();

    return total;


# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :
    playersMin = 2;
    playersMax = 4;
    playersName = ["Fabio", "Jerome", "Renaud", "Henry", "Nathaniel", "Guillaume", "Nadège"];

    # 1) Préparation du jeu domino
    # Les joueurs sont representés sur forme de liste où chaque index contient
    # un joueur différent.
    shuffle(playersName);
    playerList = [];
    nPlayers = randrange(playersMin, playersMax+1);
    for i in range(nPlayers) :
        playerList.append(Player(playersName[i]));

    # Création du plateau
    gameTable = GameTable();

    # 2) Commencement du jeu
    # 2a. Chaque joueur pioche 7 dominos pour commencer
    for player in playerList :
        for i in range(7) :
            player.addDomino(gameTable.pickupDomino());
        
        print("{} pioche 7 dominos.".format(player.getName()));
        time.sleep(0.5);

    # 2b. Établir quel joueur commence la partie
    # Le joueur disposant du plus grand domino double sera le premier à jouer
    # Le plus grand domino double de chaque joueur est stocké dans cette liste
    highestDoublesDominoes = [];
    for player in playerList :
        doubleDominoes = getDoubleDominoes(player.getHand());

        # Si le joueur ne dispose pas de dominos doubles, passer au joueur
        # suivant directement.
        if (len(doubleDominoes) == 0) :
            continue;

        maxDoubleDomino = getMaxDomino(doubleDominoes);
        highestDoublesDominoes.append(maxDoubleDomino);

    if (len(highestDoublesDominoes) != 0) :
        openingDomino = getMaxDomino(highestDoublesDominoes);

        # Sauvegarder la position du joueur, dans la liste, qui doit commencer
        playerPos = playerList.index(openingDomino.getOwner());

        print("\n{} possède le plus grand domino double ({}) !".format(openingDomino.getOwner().getName(), openingDomino));
        time.sleep(0.5);
    
    # Si la liste est vide, cela signifie qu'aucun joueur possédait de dominos doubles,
    # par conséquent chaque joueur tire un nouveau domino. Celui qui a tiré le domino
    # qui vaut le plus, commence.
    else :
        print("\n\nPersonne possède de dominos doubles, chaque joueur doit piocher un domino !\n");
        time.sleep(1.5);

        decisiveDominoes = [];        
        # En cas de ex-aequo, les joueurs retirent un domino
        exAequo = True;
        while (exAequo) :
            for player in playerList :
                # Chaque joueur tire un domino dans la pioche sans le garder
                domino = gameTable.pickupDomino(False);
                
                # Attribuer temporairement le domino au joueur qui l'a tiré,
                # pour savoir plus facilement après qui commencera.
                domino.setOwner(player);                
                decisiveDominoes.append(domino);

                print("{} pioche le domino {}.".format(player.getName(), domino));
                time.sleep(0.5);

            # Calculer combien d'autres dominos tirés ont la même valeur que le plus 'grand' domino
            openingDomino = getMaxDomino(decisiveDominoes);
            recurrences = 0;
            for i in range(len(decisiveDominoes)) :
                if (openingDomino.getValue() == decisiveDominoes[i].getValue()) :
                    recurrences += 1;

            # Si le nombre d'occurrences est égal à 1 (1 parce qu'il y toujours le plus grand domino dans les dominos tirés),
            # on peut confirmer qu'il n'y a pas de cas d'ex-aequo.
            if (recurrences == 1) :
                print("\n{} possède le plus grand domino !".format(openingDomino.getOwner().getName()));
                exAequo = False;
            else :
                print("\nExAequo ! Chaque joueur doit retirer à nouveau 1 domino...\n");
            
            time.sleep(1.5);
            
            # Sauvegarder la position du joueur, dans la liste, qui doit commencer
            playerPos = playerList.index(openingDomino.getOwner());

            # Redéfinir les dominos tirés comme appartenant à personne car ils sont toujours dans la pioche
            for i in range(len(decisiveDominoes)) :
                decisiveDominoes[i].setOwner(None);
   
    # Le joueur qui doit commencer est positionné au premier index de la liste des joueurs
    playerList[0], playerList[playerPos] = playerList[playerPos], playerList[0];

    # 3) Déroulement du jeu
    print("\n\nLe match commence.");
    endGame = False;
    while (not endGame) :    
        for player in playerList :
            player.canPlay = False;

            playerHand = player.getHand();
            for i in range(len(playerHand)) :
                # Si on peut le placer sur le jeu
                if (gameTable.placeDomino(playerHand[i])) :
                    player.canPlay = True;
        
                    print("\n\n{} joue le domino {}.\n".format(player.getName(), playerHand[i]));
                    print("* JEU *");
                    printGame(gameTable.getGame());
                    time.sleep(0.7);
                    
                    # L'effacer de la main du joueur
                    player.removeDomino(playerHand[i]);                   
                    break;

            # Si un joueur n'a plus de dominos en main ou si plus personne
            # sait jouer de dominos le jeu se termine
            if (player.hasEmptyHand()) :
                print("\n\n{} n'a plus de dominos en main ! {} gagne !".format(player.getName(), player.getName()));
                endGame = True;
                break;

            if (countPlayersAbleToPlay(playerList) == 0 and gameTable.isStockEmpty()) :
                print("\n\Plus personne sait jouer ! Le partie se cloture");
                endGame = True;
                break;

            # Si le joueur n'a pas joué pendant cette manche il doit piocher un domino
            if (not player.canPlay) :
                if (not gameTable.isStockEmpty()) :
                    domino = gameTable.pickupDomino();
                    player.addDomino(domino);

    # 3) Fin de partie
    clearConsole();
    
    # La liste est triée selon la valeur de la main de chaque joueur
    list.sort(playerList, key = lambda player : getHandValue(player.getHand()));

    # Affichage des scores
    print("SCORES : \n");
    for i in range(len(playerList)) :
        player = playerList[i];
        print("{}) {} avec {} points".format(i+1, player.name, getHandValue(player.getHand())));
