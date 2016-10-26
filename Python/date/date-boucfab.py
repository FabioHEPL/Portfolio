#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#       date-boucfab.py
#       
#       Copyright 2012 Fabio_BOUCHE_-_classe5t <boucfab@pc62>
#


# Vérifie si l'année est bissextile
def AnneeBissextile(annee) :		
	# Une année est bissextile soit quand elle est divisible par 4 mais
	# non divisible, soit divisible par 400	
	if ((annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0) :
		return True;
	else :
		return False;


# Verifie si la date est valide (c.-à-d. si le jour, mois et année existent)
def DateEstValide(jour, mois, annee, listeMois) :
	# Étant donné que la première date valide en informatique est le
	# 1 janvier 1900 il faut que l'année donnée soit plus grande ou égale à 1900.
	# De plus, il faut que le mois et jour donnés existent
	if (annee >= 1900 and mois in listeMois) :
		if (jour > 0 and jour <= listeMois[mois]) :
				return True;
	
	# Si au moins une des conditions précédentes est fausse, renvoyer False
	return False;


# Calcule le jour de la semaine à partir d'une date donnée
def JourDeLaSemaine(date) :	
	# Liste de tous les mois et les jours correspondants dans une année
	listeMois = {"janvier": 31, "fevrier": 28, "mars": 31, "avril": 30,
			"mai": 31, "juin": 30, "juillet": 31, "aout": 31,
			"septembre": 30, "octobre": 31, "novembre": 30,
			"decembre": 31};
	
	# Vu que les éléments dans un dictionnaire ne sont pas ordonnés
	# à l'exécution du script, voici un autre dictionnaire qui stocke
	# l'ordre des mois dans le dictionnaire précédent
	ordreMois = {1: "janvier", 2: "fevrier", 3: "mars", 4: "avril", 5: "mai",
				 6: "juin", 7: "juillet", 8: "aout", 9: "septembre",
				 10: "octobre", 11: "novembre", 12: "decembre"};				 
	
	listeJoursSemaine = {1:"lundi", 2:"mardi", 3:"mercredi", 4:"jeudi",
					5:"vendredi", 6:"samedi", 7:"dimanche"};
					
	
	
	# Découpe la date pour stocker le jour, mois et année dans
	# différentes variables
	date = date.split(' ');	
	jour = int(date[0]);
	mois = date[1];
	annee = int(date[2]);
		
	
	# Si l'année est bissextile, le nombre de jours dans le mois de
	# février sera égal à 29
	if (AnneeBissextile(annee)) :
		listeMois["fevrier"] = 29;		
	
	
	# Si la date entrée n'est pas valide, renvoyer "" (rien) de sorte
	# que l'utilisateur puisse entrer une nouvelle date 
	if (not DateEstValide(jour, mois, annee, listeMois)) :
		return "";
	
	
	# Calcule le nombre de jours en partant du 1 janvier de l'année donnée
	# jusqu'à la date donnée
	sommeJours = jour;
	i = 1;
	while (mois != ordreMois[i]) :
		joursDansMois = listeMois[ordreMois[i]];	
		sommeJours += joursDansMois;
		i += 1;

	
	# L'année donnée ne doit pas être comptée donc on enlève 1
	annee -= 1;
	
	# Cet algorithme permet de trouver le jour de la semaine à partir
	# d'une simple date.
	jourSemaine = (annee + (annee // 4) - (annee // 100) + (annee // 400) + sommeJours) % 7;
	
	# En utilisant cet algorithme, le nombre 0 correspondra à un dimanche.
	# Pour qu'il soit compatible avec le dictionnaire contenant les jours
	# de la semaine créé précedemment, la nouvelle valeur attribuée sera 7
	if (jourSemaine == 0) :
		jourSemaine = 7;		
		
	
	# Renvoie le jour de la semaine sous forme de chaîne
	return listeJoursSemaine[jourSemaine];
	

if __name__ == "__main__" :
	# Tant que l'utilisateur n'a pas entré une date valide ...
	while (True) :
		date = input("Entrez une date [jour mois année] : ");
		if (JourDeLaSemaine(date) != "") :
			break;
		else :
			print("La date que vous avez entrée n'est pas valide.\n");
	
	# Affichage du jour de la semaine de la date entrée
	print("Le {} est un {}.".format(date, JourDeLaSemaine(date)));
