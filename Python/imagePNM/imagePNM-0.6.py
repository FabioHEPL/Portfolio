#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BOUCHÉ Fabio 6TB
# imagePNM-0.6.py – date 02.11.2013

from random import randrange

PBM = 1;
PGM = 2;
PPM = 3;

def rotation90ah(image) :
	# 1) Récuperer l'extension du fichier
	extension = "";		
	i = len(image)-1;
	while (image[i] != '.') :
		extension = image[i] + extension;
		i -= 1;

	# 2) Déterminer le nombre d'infos à chercher dans l'en-tête
	nbInfos = 4;	
	if (extension == "pbm") :
		nbInfos = 3;	 
	
	fichier = open(image, 'r+');	
	
	# 3) Récuperer les informations contenue dans l'en-tête
	enTete = readInfo(fichier, nbInfos);
	
	# 4) Stocker le contenu de l'image dans une liste, où la valeur de
	#    chaque pixel sera un élément de la liste
	contenu = [];
	
	# Calculer le nombre de pixels en total
	largeur, hauteur = int(enTete[1]), int(enTete[2]);
	nbPixels = largeur * hauteur; 
	
	# Pour les images en format ppm, créer une sous liste pour chaque
	# pixel puisqu'il est codé sur 3 valeurs
	if (extension == "ppm") :
		for i in range(nbPixels) :
			contenu.append(readInfo(fichier, 3));
	else :
		contenu = readInfo(fichier, nbPixels);		
		
	fichier.close();
	
	# 5) Tourner l'image de 90° dans le sens anti-horloger
	contenuNewImg = [];
	for i in range(largeur-1, -1, -1) :
		for j in range(0, hauteur) :
			contenuNewImg.append(contenu[i+(largeur*j)]);
	
	# 6) Créer le fichier de l'image tournée
	nomImage = "{}_90".format(image[0:len(image)-(len(extension)+1)]);
	print(nomImage);
	
	# Écrire l'en-tête
	if (extension == "pbm") :
		image_header(hauteur, largeur, PBM, nomImage);
	elif (extension == "pgm") :
		image_header(hauteur, largeur, PGM, nomImage);
	elif (extension == "ppm") :
		image_header(hauteur, largeur, PPM, nomImage);
	
	imageTournee = open("{}.{}".format(nomImage, extension), 'a');
	
	# Écrire le contenu
	if (extension == "pbm") :
		writeImage(imageTournee, hauteur, largeur, contenuNewImg, 1);
	else :
		writeImage(imageTournee, hauteur, largeur, contenuNewImg, 3);
	
	imageTournee.close();


def desaturation_simple(ic) :
	fichier = open(ic, 'r+');	
	
	# 1) Récuperer les informations contenue dans l'en-tête
	enTete = readInfo(fichier, 4);
	
	# Si l'image n'est pas de format ppm arrêter la fonction
	if (enTete[0] != "P3") :
		return -1;
	
	# 2) Stocker le contenu de l'image dans une liste, où la valeur de
	#    chaque pixel sera un élément de la liste
	contenu = [];
	
	# Calculer le nombre de pixels en total
	largeur, hauteur = int(enTete[1]), int(enTete[2]);
	nbPixels = largeur * hauteur; 
	
	# Pour les images en format ppm, créer une sous liste pour chaque
	# pixel puisqu'il est codé sur 3 valeurs
	for i in range(nbPixels) :
		contenu.append(readInfo(fichier, 3));
	
	fichier.close();
	
	# 3) Appliquer la désaturation simple sur l'image
	contenuNewImg = [];
	for i in range(len(contenu)) :
		# Calculer la désaturation
		rouge = round((int(contenu[i][0]) / 100) * 30);
		vert = round((int(contenu[i][1]) / 100) * 59);
		bleu = round((int(contenu[i][2]) / 100) * 11);
			
		gris = rouge + vert + bleu;
		
		contenuNewImg.append(str(gris));		
	
	# 4) Créer le fichier de l'image désaturée	
	# Récuperer le nom de l'image
	pos = 0;	
	for i in range(len(ic)-1, -1, -1) :
		if (ic[i] == '.') :
			pos = i;
			break;
	
	nomImage = ic[0:pos];

	# Écrire l'en-tête
	image_header(largeur, hauteur, PGM, nomImage);
	
	imageDesaturee = open("{}.pgm".format(nomImage), 'a');
	
	# Écrire le contenu
	writeImage(imageDesaturee, largeur, hauteur, contenuNewImg, 3);
	
	imageDesaturee.close();


def readInfo(img, nbInfos) :
	# Les informations contenues dans l'en-tête sont stockées dans
	# cette liste
	infosImage = [];
	
	# Indique si le caractère lu est le premier d'une nouvelle ligne
	debutLigne = True;
	# Variable temporaire qui stocke une information à la fois pour
	# l'insérer ensuite dans la liste
	info = "";
		
	while (len(infosImage) < nbInfos) :
		# Lire le fichier un caractère à la fois
		tmp = img.read(1);
		
		# Vérifier si la ligne est un commentaire
		if (debutLigne) :			
			debutLigne = False;
			
			# Si la ligne est un commentaire, la sauter
			if (tmp == '#') :
				img.readline();
				continue;		
		
		# Les différentes informations sont délimitées par des espaces
		# ou retours à la ligne, on construit une information à la fois
		# à partir de cela
		if (tmp != ' ' and tmp != '\n') :
			info += tmp;
		else :
			if (info != '') :				
				infosImage.append(info);
				info = "";
				
			# Si le caractère lu est un retour à la ligne, cela signifie
			# que le prochain sera le premier d'une nouvelle ligne
			if (tmp == '\n') :
				debutLigne = True;

	return infosImage;


def writeImage(img, largeur, hauteur, contenu, ecart) :
	index = 0;
	for i in range(hauteur) :
		for j in range(largeur) :
			if (j == 0) :
				img.write("{:>{e}}".format(contenu[index], e=ecart));
			else :
				img.write(" {:>{e}}".format(contenu[index], e=ecart));
			index += 1;
			
		img.write('\n');


def create_coloredpx(image) :
	# 1) Récuperer l'extension du fichier
	extension = "";		
	i = len(image)-1;
	while (image[i] != '.') :
		extension = image[i] + extension;
		i -= 1;

	# 2) Déterminer le nombre d'infos à chercher dans l'en-tête
	nbInfos = 4;	
	if (extension == "pbm") :
		nbInfos = 3;	 
	
	fichier = open(image, 'r+');	
	
	# 3) Récuperer les informations contenue dans l'en-tête
	enTete = readInfo(fichier, nbInfos);
	
	# 4) Stocker le contenu de l'image dans une liste, où la valeur de
	#    chaque pixel sera un élément de la liste
	contenu = [];
	
	# Calculer le nombre de pixels en total
	largeur, hauteur = int(enTete[1]), int(enTete[2]);
	nbPixels = largeur * hauteur; 
	
	# Pour les images en format ppm, créer une sous liste pour chaque
	# pixel puisqu'il est codé sur 3 valeurs
	if (extension == "ppm") :
		for i in range(nbPixels) :
			contenu.append(readInfo(fichier, 3));
	else :
		contenu = readInfo(fichier, nbPixels);		
		
	fichier.close();

	# 5) Tirer aléatoirement les 20% de pixels et modifier leur(s) valeur(s)
	pourcentage = 20;
	
	# Calculer le nombre de pixels aléatoires qu'il faut modifier	
	nbPixelsAleatoires = round((nbPixels / 100) * pourcentage);
	
	# Stocker les index des pixels aléatoires dans une liste
	idPixels = []; 
	
	i = 0;
	while (i < nbPixelsAleatoires) :
		element = randrange(0, nbPixels);		
		# On ne peut pas tirer deux fois le même pixel
		if (not element in idPixels) :
			idPixels.append(element);			
			i += 1;
		
	# 6) Modifier l'image de départ avec les pixels colorés et réecrire l'image
	if (extension == "pbm") :
		# En noir et blanc, la couleur des pixels tirés aléatoirement
		# sera noir si le fond est blanc, blanc si le fond est noir.
		for i in range(len(idPixels)) :
			if (contenu[idPixels[i]] == '0') :
				contenu[idPixels[i]] = '1';
			else :
				contenu[idPixels[i]] = '0';
		
		image_header(largeur, hauteur, PBM);
	
	elif (extension == "pgm") :
		# En nuance de gris, la couleur des pixels tirés aléatoirement
		# sera également tirée aléatoirement soit entre 1 et 255 si la
		# couleur de fond choisie est 0, soit entre 0 et 254 si la
		# couleur de fond choisie est 255.
		for i in range(len(idPixels)) :
			if (contenu[idPixels[i]] == '0') :
				contenu[idPixels[i]] = str(randrange(1, 256));
			elif (contenu[idPixels[i]] == '255') :
				contenu[idPixels[i]] = str(randrange(0, 255));
		
		image_header(largeur, hauteur, PGM);	
		
	elif (extension == "ppm") :
		# En couleur RVB, la couleur des pixels tirés aléatoirement sera
		# également tirée au hasard. Chaque composante d'une couleur
		# sera tirée au hasard également.
		for i in range(len(idPixels)) :
			for j in range(3) :
				contenu[idPixels[i]][j] = str(randrange(0, 256));
				
		image_header(largeur, hauteur, PPM);
		
		# Reformatter le contenu des images ppm pour la fonction writeImage
		tmp = [];
		for i in range(len(contenu)) :
			tmp.append("{:>3} {:>3} {:>3}".format(contenu[i][0], contenu[i][1], contenu[i][2]));
		contenu = tmp;	
		
	fichier = open(image, 'a');

	# Réecrire le contenu
	if (extension == "pbm") :
		writeImage(fichier, largeur, hauteur, contenu, 1);
	else :
		writeImage(fichier, largeur, hauteur, contenu, 3);
	
	fichier.close();
	

def image_header(largeur, hauteur, type, nom="image") :
	enTetes = {
	PBM:{"extension":"pbm", "nombreMagique":"P1", "valMaximale":''},
	PGM:{"extension":"pgm", "nombreMagique":"P2", "valMaximale":"255\n"},
	PPM:{"extension":"ppm", "nombreMagique":"P3", "valMaximale":"255\n"}
	}
	
	# Créer le fichier image avec la bonne extension
	fichier = open("{}.{}".format(nom, enTetes[type]["extension"]), "w+");
	
	# Nombre magique
	fichier.write("{}\n".format(enTetes[type]["nombreMagique"]));
	
	# Écrire le commentaire d'en-tête	
	fichier.write("# image créée par imagePNM.py (BOUCHÉ Fabio, Copyright 2013)\n");
	
	# Largeur et hauteur
	fichier.write("{} ".format(str(largeur)));
	fichier.write("{}".format(str(hauteur)));
	
	# Valeur maximale
	fichier.write("\n{}".format(enTetes[type]["valMaximale"]));
	
	fichier.close();


def create_image(largeur, hauteur, type) :
	image_header(largeur, hauteur, type);
	
	if (type == PBM) :
		create_pbm(largeur, hauteur);
	elif (type == PGM) :
		create_pgm(largeur, hauteur);
	elif (type == PPM) :
		create_ppm(largeur, hauteur);


def create_pbm(largeur, hauteur) :
	fichier = open("image.pbm", "a");
	
    # Écrire contenu (fond blanc)
	for i in range(hauteur) :
		for j in range(largeur) :
			if (j == 0) :
				fichier.write('0');
			else :
				fichier.write(' 0');
		fichier.write('\n');
	
	fichier.close();


def create_pgm(largeur, hauteur) :
	fichier = open("image.pgm", "a");
	
	# Écrire contenu (fond blanc)
	for i in range(hauteur) :
		for j in range(largeur) :
			if (j == 0) :
				fichier.write('255');
			else :
				fichier.write(' 255');
		fichier.write('\n');
	
	fichier.close();
	

def create_ppm(largeur, hauteur) :
	fichier = open("image.ppm", "a");
	
	# Écrire contenu (fond blanc)
	for i in range(hauteur) :
		for j in range(largeur) :
			if (j == 0) :
				fichier.write('255 255 255');
			else :
				fichier.write(' 255 255 255');
		fichier.write('\n');
	
	fichier.close();


if __name__ == "__main__" :
	nom_image = "img/blackbuck.ppm";
	rotation90ah(nom_image);
	
