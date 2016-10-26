-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Ven 13 Juin 2014 à 05:52
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `boucfab_db`
--
CREATE DATABASE IF NOT EXISTS `boucfab_db` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `boucfab_db`;

-- --------------------------------------------------------

--
-- Structure de la table `articles`
--

CREATE TABLE IF NOT EXISTS `articles` (
  `id_article` int(11) NOT NULL AUTO_INCREMENT,
  `code_article` varchar(6) NOT NULL,
  `nom` varchar(40) NOT NULL,
  `prix` float NOT NULL,
  `largeur` int(11) NOT NULL,
  `hauteur` int(11) NOT NULL,
  `categorie` varchar(40) NOT NULL,
  `image` varchar(60) NOT NULL,
  `quantite` int(11) NOT NULL,
  PRIMARY KEY (`id_article`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Contenu de la table `articles`
--

INSERT INTO `articles` (`id_article`, `code_article`, `nom`, `prix`, `largeur`, `hauteur`, `categorie`, `image`, `quantite`) VALUES
(1, 'A1000', 'The Beatles', 6.99, 30, 20, 'musique', '/LPoster/images/articles/art01.jpg', 20),
(2, 'A1001', 'STAR WARS - Empire Needs You  ', 9.99, 24, 36, 'film', '/LPoster/images/articles/art02.jpg', 3),
(3, 'A1002', 'Ha Ha', 10.99, 24, 36, 'film', '/LPoster/images/articles/art03.jpg', 1),
(4, 'A1003', 'Django Unchained', 8.99, 24, 36, 'film', '/LPoster/images/articles/art04.jpg', 1),
(5, 'A1004', 'The X-Files', 13.5, 22, 30, 'film', '/LPoster/images/articles/art05.jpg', 1),
(6, 'A1005', 'The Godfather ', 13.5, 22, 30, 'film', '/LPoster/images/articles/art06.jpg', 1),
(7, 'A1006', 'The Chimp Stereo', 13.5, 22, 30, 'film', '/LPoster/images/articles/art07.jpg', 1),
(8, 'A1007', 'Rolling Stones', 13.5, 22, 30, 'film', '/LPoster/images/articles/art08.jpg', 1);

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

CREATE TABLE IF NOT EXISTS `clients` (
  `id_client` int(11) NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(30) NOT NULL,
  `mdp` varchar(50) NOT NULL,
  `email` varchar(40) NOT NULL,
  `adresse` varchar(40) NOT NULL,
  `telephone` varchar(30) NOT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Contenu de la table `clients`
--

INSERT INTO `clients` (`id_client`, `pseudo`, `mdp`, `email`, `adresse`, `telephone`) VALUES
(1, 'Fabbb', '4fded1464736e77865df232cbcb4cd19', '', '', ''),
(2, 'FabioTest', '900150983cd24fb0d6963f7d28e17f72', '', '', ''),
(3, 'Fofo', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(4, 'Okc', '14b8f0494c6f1460c3720d0ce692dbca', '', '', ''),
(6, 'HEY', 'brry2050', '', '', ''),
(7, 'Fabio', 'test2', 'yolo@hot', 'okok', 'no'),
(8, 'Fabio"', 'd58e3582afa99040e27b92b13c8f2280', '', '', ''),
(9, 'TestCo', '4fded1464736e77865df232cbcb4cd19', '', '', ''),
(10, 'hozoNe', '4fded1464736e77865df232cbcb4cd19', '', '', ''),
(11, 'Fred', '7682fe272099ea26efe39c890b33675b', 'freddy@gmail.com', 'Rue Jean-Yves, 1/12', '0470561198'),
(12, '', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(13, 'sdf', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(14, 'sdfsdsdfsdf', 'd194f6194fc458544482bbb8f0b74c6b', '', '', ''),
(15, 'sdffds', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(16, 'sdfdfs', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(17, 'sdfsdf', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(18, 'Frede', 'fc848409f5efeeee876426275569f4d2', '', '', ''),
(19, 'Mauvais', '6b427a0714bf7a267e81364f7f5c224a', '', 'Maisouiok', '0470561198');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
