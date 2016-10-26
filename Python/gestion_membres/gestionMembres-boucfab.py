#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BOUCHÉ Fabio 6TB
# gestionMembres-boucfab.py – date 17.09.2013

import sys
import os
import time

# ----------------------------------------------------------------------
# @ FONCTIONS PERSO
# ----------------------------------------------------------------------
# Efface ce qu'il y a écrit dans la console
def clearConsole() :
    if (sys.platform == "win32") :
        os.system("cls");
    elif (sys.platform == "linux2") :
        os.system("clear"); 


# Simule l'animation d'un chargement
def simulerChargement(nombrePoints, dureeTotale) :
	duree = dureeTotale / nombrePoints;
	
	for i in range(nombrePoints) :
		sys.stdout.write(".");
		time.sleep(duree);
		sys.stdout.flush();


# Efface toutes les lignes corrompues dans le fichier
def reparerFichier(fiche, enTete) :
	fichier = open(fiche, 'r+');
		
	# 1) Insérer l'en-tête
	contenu = [enTete + '\n'];	
		
	# Passer la première ligne car elle contient l'en-tête
	for ligne in fichier :
		break;
		
	# Calculer le nombre de colonnes correspondantes à l'en-tête
	nombreColonnes = 1;
	for i in range(len(enTete)) :
		if (enTete[i] == ';') :
			nombreColonnes += 1;	
	
	# 2) Vérifier que chaque ligne possède le nombre correct d'informations
	for ligne in fichier :
		ligne = ligne.split(';');
		
		# On vérifie que le nombre d'informations fourni sur le membre
		# est correct
		if (len(ligne) == nombreColonnes) :
			# On enlève les espace de debut et fin de chaque ligne
			for i in range(len(ligne)) :
				ligne[i] = ligne[i].strip();
			
			nouvelleLigne = ';'.join(ligne) + '\n';
			contenu.append(nouvelleLigne)	
		
	fichier.close();
	
	# 3) On réecrit le fichier avec seulement les lignes valide
	fichier = open(nomFichier, 'w+');
	
	fichier.writelines(contenu);
	
	fichier.close();


# ----------------------------------------------------------------------
# @ FONCTIONS GESTION MEMBRES
# ----------------------------------------------------------------------
# Affiche le menu de gestion de la liste des membres
def menu() :
	print("""+-------------------------------------+
|    GESTION DE LISTE DE MEMBRES      |
+-------------------------------------+
| Bienvenue,                          |
| Que désirez-vous faire ?            |
|                                     |
| 1. Afficher tous les membres.       |
| 2. Ajouter un nouveau membre.       |
| 3. Modifier un membre existant.     |
| 4. Supprimer un membre existant.    |
| 5. Supprimer tous les membres.      |
+-------------------------------------+
| 6. Quitter l'application.           |
+-------------------------------------+""");


# Affiche la liste des membres faisant partie du club et leurs cordonnées
def afficherTout(fiche, enTete) :
	# L'écart entre les différentes colonnes
	ecartColonnes = 3;
	# La largeur absolue qu'une colonne ne peut pas dépasser en aucun cas
	largeurAbsolue = 50;
	
	fichier = open(fiche, 'r');	
	
	enTete = enTete.split(';');	
	# On ajoute la colonne ligne qui sera utilisée lors de l'affichage
	enTete.insert(0, "LIGNE");
	
	# On saute la première ligne car c'est l'en-tête
	for ligne in fichier :
		break;
	
	# 1) Stocker le contenu du fichier
	contenu = [];
	numeroLigne = 2;
	for ligne in fichier :
		donnees = ligne.split(';');
		contenu.append([str(numeroLigne)] + donnees);

		numeroLigne += 1;
	
	# Toutes les informations sur chaque colonne seront regroupées dans
	# cette liste
	colonnes = [];	
	for i in range(len(enTete)) :
		colonnes.append({});
		colonnes[i]["nom"] = enTete[i];
		
		# 2) Calculer la largeur maximale de chaque colonne
		# La largeur maximale par défaut d'une colonne c'est la longueur
		# de l'en-tête de cette dernière
		largeurMaximale = len(enTete[i]);
		
		for j in range(len(contenu)) :
			largeurChaine = len(contenu[j][i]);
			
			if (largeurChaine > largeurMaximale) :
				largeurMaximale = largeurChaine;
		
			if (largeurMaximale > largeurAbsolue) :
				largeurMaximale = largeurAbsolue;
		
		colonnes[i]["largeur"] = largeurMaximale + ecartColonnes;		
		
	# 3) Affichage des colonnes
	# On affiche d'abord les en-têtes des colonnes
	for colonne in colonnes :
		print("{0:<{l}}".format(colonne["nom"][0:largeurAbsolue], l=colonne["largeur"]), end="");	
	print("\n");
	
	# On affiche ensuite le contenu des colonnes
	for i in range(len(contenu)) :
		for j in range(len(contenu[i])) :
			print("{:<{l}}".format(contenu[i][j][0:largeurAbsolue], l=colonnes[j]["largeur"]), end="");
		print("\n");
	
	fichier.close();


# Ajoute un nouveau membre à la liste des membres
def insererMembre(fiche, membre) :
	fichier = open(nomFichier, 'a');
	
	# On créé la ligne avec les données du membre à stocker dans le fichier
	ligneMembre = ';'.join(membre) + '\n';
		
	fichier.write(ligneMembre);
	
	fichier.close();


# Modifie les cordonnées d'un membre existant
def modifierMembre(fiche, numLigne, membre) :
	fichier = open(fiche, 'r');
	
	# On créé la ligne avec les données du membre à stocker dans le fichier
	ligneMembre = ';'.join(membre) + '\n';
	
	# On stocke tout le contenu du fichier sauf la ligne du membre
	# à modifier qui sera remplacée avec les nouvelles données
	contenu = [];
	cptLignes = 1;
	for ligne in fichier :
		if (cptLignes != numLigne) :
			contenu.append(ligne);
		else :
			contenu.append(ligneMembre);	
			
		cptLignes += 1;	
	
	fichier.close();
	
	# On réecrit le fichier avec les nouvelles données
	fichier = open(fiche, 'w+');
	
	fichier.writelines(contenu);
	
	fichier.close();


# Enlève un membre du club
def supprimerMembre(fiche, numLigne) :
	fichier = open(fiche, 'r');
	
	# On stocke tout le contenu du fichier sauf la ligne du membre
	# à supprimer
	contenu = [];
	cptLignes = 1;
	for ligne in fichier :
		if (cptLignes != numLigne) :
			contenu.append(ligne);
			
		cptLignes += 1;	
	
	fichier.close();
	
	# On réecrit le fichier avec les nouvelles données
	fichier = open(fiche, 'w+');
	
	fichier.writelines(contenu);
	
	fichier.close();


# Enlève tous les membres faisant partie du club	
def supprimerTout(fiche) :
	# On efface tout le contenu du fichier
	fichier = open(fiche, 'w+');
	fichier.close();


# ----------------------------------------------------------------------
# @ MAIN
# ----------------------------------------------------------------------
if __name__ == "__main__" :
	# Le nom du fichier
	nomFichier = "fiche";
	
	# L'en-tête du fichier par défaut
	enTete = "NOM;PRENOM;ADRESSE;CP;LOCALITÉ;DATE NAISSANCE";
	
	# Les différents champs que l'on retrouve lors de l'insertion/modification
	# d'un membre
	champs = ["Nom du membre", "Prénom du membre", "Adresse",
		      "Code postal", "Localité", "Date de naissance"];
		
	# Les informations sur les fonctions qui doivent apparaître dans le menu
	# sont stockées dans une liste
	fonctions = {
	1:{"nom":"afficherTout", "description":"Afficher tous les membres"},
	2:{"nom":"insererMembre", "description":"Ajouter un nouveau membre"},
	3:{"nom":"modifierMembre", "description":"Modifier un membre existant"},
	4:{"nom":"supprimerMembre", "description":"Supprimer un membre existant"},
	5:{"nom":"supprimerTout", "description":"Supprimer tous les membres"},
	6:{"nom":"quitterApplication", "description":"Quitter l'application"}
	};
	
	# Création/Vérification du fichier
	fichier = open(nomFichier, 'w');
	reparerFichier(nomFichier, enTete);
	fichier.close();
	
	# Le menu va être affiché tant que l'utilisateur ne quitte pas l'application
	afficherMenu = True;
	while (afficherMenu) :
		clearConsole();
		
		# 1) Affichage du menu
		menu();
		
		# 2) L'utilisateur choisi quelle fonction exécuter
		numFonction = input("\nVotre choix : ");
		
		# * Vérification de données : si l'utilisateur ne choisi pas
		# l'une des fonctions proposées, retourner au menu
		if (not numFonction.isdigit()) :
			continue;
		else :
			numFonction = int(numFonction);
				
		if (numFonction < 0 or numFonction > len(fonctions)) :
			continue;
						
		# 3) La fonction est executée
		print("\nL'entrée \"{}. {}\" a été sélectionnée".format(numFonction, fonctions[numFonction]["description"]), end=" ");
		simulerChargement(4, 2);
		clearConsole();
		
		# - Afficher Tout
		if (numFonction == 1) :
			reparerFichier(nomFichier, enTete);
			afficherTout(nomFichier, enTete);
			
		# - Insérer Membre
		elif (numFonction == 2) :
			reparerFichier(nomFichier, enTete);
						
			while (True) :
				clearConsole();
				
				print("Désirez-vous ajouter un membre ? (O/n)");
				choix = input("Votre choix : ");
				print("");
				
				if (choix != '' and choix != 'O' and choix != 'o') :
					break;
				
				# Les données du membre sont stockées sur forme de liste
				# avant l'insertion
				donnees = [];
				for i in range(len(champs)) :
					reponse = input("* {} : ".format(champs[i]));
					reponse = reponse.strip();
					donnees.append(reponse);
					
				insererMembre(nomFichier, donnees);
					
				print("");
				simulerChargement(4, 1);				
				print("\n\nMerci ! Le membre \"{} {}\" a été ajouté avec succès !".format(donnees[1], donnees[0]));
					
				time.sleep(2.5);
		
		# - Modifier Membre
		elif (numFonction == 3) :
			reparerFichier(nomFichier, enTete);
			afficherTout(nomFichier, enTete);
			
			idLigne = int(input("\nSelectionnez le membre que vous voulez modifier (tapez le numero de la ligne corréspondante) : "));
			
			# Récup données membre
			fichier = open(nomFichier, 'r');
			
			numeroLigne = 1;
			for ligne in fichier :				
				if (numeroLigne == idLigne) :
					donnees = ligne.split(';'); 
				
				numeroLigne += 1;			
			
			fichier.close();						
			
			# Modification du membre
			nouvellesDonnees = [''] * len(donnees);
			for i in range(len(nouvellesDonnees)+1) :
				clearConsole();
				
				print("Modification du membre '{} {}' :".format(donnees[1], donnees[0]));
				print("- Appuyez sur 'Entrée' pour passer au champ suivant.");
				print("- Ne tapez rien si vous voulez que le champ ne soit pas modifié.\n");	
				
				for j in range(i) :
					print("* {} : {}".format(champs[j], nouvellesDonnees[j]));
					
				if (i != len(nouvellesDonnees)) :
					reponse = input("* {} : ".format(champs[i]));
					
					if (reponse != '') :
						nouvellesDonnees[i] = reponse;
					else :
						nouvellesDonnees[i] = donnees[i];
	
			modifierMembre(nomFichier, idLigne, nouvellesDonnees);
		
		# - Supprimer Membre
		elif (numFonction == 4) :
			reparerFichier(nomFichier, enTete);
			afficherTout(nomFichier, enTete);
			
			idLigne = int(input("\nSelectionnez le membre que vous voulez supprimer (tapez le numero de la ligne corréspondante) : "));
			
			supprimerMembre(nomFichier, idLigne);
			
			print("\nMembre supprimé correctement.\n");
			
		# - Supprimer Tout
		elif (numFonction == 5) :
			supprimerTout(nomFichier);
			# On réecrit l'en-tête
			reparerFichier(nomFichier, enTete);
			
			print("Tous les membres ont été supprimés.\n");
			
		# - Quitter Application
		elif (numFonction == 6) :
			afficherMenu = False;
			continue;
		
		# 4) Retour au menu
		input("\nAppuyez sur Entrée pour retourne au menu ...");		
