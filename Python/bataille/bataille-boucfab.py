#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       bataille-boucfab.py
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc62>
#


import time
import os
from random import randrange


def Creation(jeu) :
	# le nombre de couleurs différentes qu'il y a dans le jeu
	max_couleurs = 4;
		
	# boucle qui remplit la liste de tuples contenant la valeur et
	# couleur des différentes cartes
	for i in range(max_couleurs) :
		for j in range(2, 15) :
			jeu.append((j, i));


def Battre(jeu) :
	listeMelangee = [];
		
	i = len(jeu);		
	while (i != 0) :
		# tire au sort un nombre de 0 à 52(taille du jeu) pas compris
		elementAleatoire = randrange(0, len(jeu));
		
		# copie l'élement aléatoire dans la liste mélangée et l'efface
		# de la vieille liste
		listeMelangee.append(jeu[elementAleatoire]);			
		del(jeu[elementAleatoire]);
		
		# i est égal à la taille de la vieille liste dont on retire les cartes,
		# quand elle sera vide(taille = 0) la boucle s'arrêtera
		i = len(jeu);
		
	# renvoie la liste melangée
	return listeMelangee;
		
		
def Couper(jeu) :
	premiereListe = [];
	deuxiemeListe = [];
	
	for i in range(len(jeu)) :
		if (i % 2 == 0) :
			premiereListe.append(jeu[i]);
		else :
			deuxiemeListe.append(jeu[i]);
			
	jeuMelange = [premiereListe, deuxiemeListe];	
	return jeuMelange;


def RemporterManche(gagnant, perdant, bataille, nomGagnant) :
	if (len(bataille) != 0) :
		print("{} gagne la bataille et remporte les {} cartes !\n\n".format(nomGagnant, len(bataille)+2));		 
		
		# ajoute les cartes gagnées avec la bataille à la liste du gagnant
		for i in range(len(bataille)) :
			gagnant.append(bataille[i]);			
	else :
		print("{} remporte la manche !\n\n".format(nomGagnant));		
	

	# ajoute les deux cartes jouées à la liste du gagnant
	gagnant.append(gagnant[0]);
	gagnant.append(perdant[0]);
	
	# éfface les deux cartes jouées du jeu des joueurs
	del(gagnant[0]);
	del(perdant[0]);

		
def Tirer(jeu, joueurs) :
	listeBataille = [];	
	os.system("cls");
	
	print("Le match commence !\n");	
	
	while (len(jeu[0]) > 0 and len(jeu[1]) > 0) :
		# affiche à l'écran les deux cartes tirées
		print("{} VS {}".format(NomCarte(jeu[0][0]), NomCarte(jeu[1][0])));
		time.sleep(0.5);
		
		# le joueur n°1 gagne
		if (jeu[0][0][0] > jeu[1][0][0]) :
			RemporterManche(jeu[0], jeu[1], listeBataille, joueurs[0][0]);
			joueurs[0][1] += 1;
			listeBataille = [];			
			
		# le joueur n°2 gagne	
		elif (jeu[0][0][0] < jeu[1][0][0]) :
			RemporterManche(jeu[1], jeu[0], listeBataille, joueurs[1][0]);
			joueurs[1][1] += 1;
			listeBataille = [];		
			
		# bataille (égalité), les deux cartes sont les mêmes
		else :
			print("Bataille !\n\n");
			
			# stocke les deux cartes jouées dans la liste bataille
			listeBataille.append(jeu[0][0]);
			listeBataille.append(jeu[1][0]);
			
			# éfface les deux cartes jouées du jeu des joueurs
			del(jeu[0][0]);
			del(jeu[1][0]);
		
		time.sleep(1);

	
	# renvoie -1 si le match est nul
	if (len(listeBataille) != 0) :
		return -1;
	else :
		# renvoie 0 si le joueur n°1 a gagné
		if (len(jeu[0]) != 0) :
			return 0;
		# renvoie 1 si le joueur n°2 a gagné
		elif (len(jeu[1]) != 0) :
			return 1;
	
	
def NomCarte(carte) :
	return valeurs[carte[0]] + " de " + couleurs[carte[1]];
	

if __name__ == "__main__":
	couleurs = { 0:"Trèfle", 1:"Pique", 2:"Carreau", 3:"Coeur" };
	valeurs = { 2:"Deux", 3:"Trois", 4:"Quatre", 5:"Cinq", 6:"Six", 7:"Sept",
				8:"Huit", 9:"Neuf", 10:"Dix", 11:"Valet", 12:"Dame", 13:"Roi", 14:"As" };

	rejouer = True;
	while (rejouer) :
		os.system("cls");
		
		jeuDeCartes = [];	
		joueurs = [["joueur n°1", 0], ["joueur n°2", 0]];
		gagnant = 0;
		
		choisirNom = True;	
		if (choisirNom) :
			for i in range(len(joueurs)) :
				joueurs[i][0] = input("Entrez le nom du joueur n°{} : ".format(i+1))		
		
		
		# 1. Crée le jeu de cartes
		Creation(jeuDeCartes);	
		
		# 2. Mélange le jeu
		jeuDeCartes = Battre(jeuDeCartes);	
		
		# 3. Coupe le jeu (distribue le jeu aux deux joueurs)
		jeuDeCartes = Couper(jeuDeCartes);

		# 4. Tire les cartes
		gagnant = Tirer(jeuDeCartes, joueurs);
		
		# 5. Affiche resultat
		if(gagnant == 0) :
			print("{} n'a plus de cartes...\n\n\n".format(joueurs[1][0]));
			time.sleep(1.5);
			print("{} gagne avec {} manches remportées !".format(joueurs[0][0], joueurs[0][1]));
		elif (gagnant == 1) :
			print("{} n'a plus de cartes...\n\n\n".format(joueurs[0][0]));
			time.sleep(1.5);
			print("{} gagne avec {} manches remportées !".format(joueurs[1][0], joueurs[1][1]));
		else :
			print("Match nul ! Pas de gagnant !");
			print("{} a remporté {} manches.".format(joueurs[0][0], joueurs[0][1]));
			print("{} a remporté {} manches.".format(joueurs[1][0], joueurs[1][1]));
	
		
		#6. Rejoue
		rejouer = False;
		
		reponse = input("\nVoulez-vous rejouer [oui/non] : ");
		if (reponse == "oui" or reponse == "o") :
			rejouer = True;

