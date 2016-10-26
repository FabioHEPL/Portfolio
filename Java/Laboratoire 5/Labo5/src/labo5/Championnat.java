package labo5;

import nhpack.Console;

public class Championnat
{
    public static void main(String[] args)
    {        
        // Choix du nombre d'equipes qui participent au championnat
        int nombreParticipants = Integer.parseInt(Console.readLine("Encodez le nombre de equipes : "));
        while (nombreParticipants % 2 != 0 || nombreParticipants < 2)
        {
            System.out.print("Le nombre de equipes doit être pair et de deux au minimum.\n\n");            
            nombreParticipants = Integer.parseInt(Console.readLine("Encodez le nombre de equipes : "));
        }
        
        System.out.print("\n");
                
        // Encodage des noms des équipes
        String equipes[] = new String[nombreParticipants];
        for (int i = 0; i < nombreParticipants; i++)
            equipes[i] = Console.readLine(String.format("Encodez le nom de l'équipe N°%d : ", i+1));
                        
        // Mélange les participants dans le tableau pour obtenir un ordre aléatoire      
        for (int i = 0; i < equipes.length; i++)
            // Permuter un élément tiré aléatoirement avec l'élément à l'index i
            Tableaux.permuter(equipes, i, nombreAleatoire(i, equipes.length-1));
        
        // Génère les rencontres entre les différentes équipes
        int[][] matches = Tableaux.genererRencontres(equipes.length);
        
        // Boucle principale pour le menu
        boolean continuer = true;
        while (continuer)
        {            
            // Affichage du menu
            System.out.printf("\n%s\n", dessinerLigne(50, '-'));
            System.out.printf("%22s%s%22s", "", "MENU", "");
            System.out.printf("\n%s\n", dessinerLigne(50, '-'));
            
            System.out.printf("1. Afficher la liste des participants\n");
            System.out.printf("2. Afficher les recontres de la semaine\n");
            System.out.printf("3. Afficher les recontres d'un participant\n");
            System.out.print("4. Quitter\n\n");
            
            System.out.printf("%s\n\n", dessinerLigne(50, '-'));
            
            // Récupère l'option choisie par l'utilisateur dans le menu
            int choix = Integer.parseInt(Console.readLine("Votre choix : "));
            System.out.print("\n");
            
            switch (choix) 
            {                
                case 1:                    
                    // Affichage de la liste des participants
                    System.out.printf("%s\n", dessinerLigne(30, '-'));
                    System.out.print("LISTE PARTICIPANTS");
                    System.out.printf("\n%s\n", dessinerLigne(30, '-'));
                    
                    for (int i = 0; i < equipes.length; i++)
                        System.out.printf("%d. %s\n", i+1, equipes[i]);

                    System.out.printf("\n%s\n", dessinerLigne(30, '-'));                                      
                    
                    break;
                
                    
                case 2:
                    // Affichage des rencontres de la semaine                    
                    System.out.printf("%s\n", dessinerLigne(110, '-'));
                    
                    for (int i = 0; i < matches.length-1; i++)
                    {
                        System.out.printf("%-15s", String.format("JOUR %s", i+1));     
                        
                        // Parcourt le "triangle" dans le tableau définissant
                        // les rencontres entre les différentes équipes
                        for (int j = 0; j < matches.length-1; j++)
                        {
                            for (int k = 1 + j; k < matches.length; k++)
                            {
                                if (matches[j][k] == i+1)                    
                                    System.out.printf("%-35s", String.format("%s vs %s", equipes[j], equipes[k]));                    
                            }                
                        }            
                        
                        System.out.printf("\n%s\n", dessinerLigne(110, '-'));
                    }   

                    break;
                    
                    
                case 3:                   
                    String participant = Console.readLine("Entrez le nom de l'équipe : ");
                    int idEquipe = indexParticipant(participant, equipes);
                    
                    // Vérifie que le nom d'équipe qui a été rentré est valide
                    while ((idEquipe = indexParticipant(participant, equipes)) == -1)
                    {
                        System.out.print("Le nom de l'équipe n'a pas été trouvé dans la liste des participants.\n\n");
                        participant = Console.readLine("Entrez le nom de l'équipe : ");
                    }
                    
                    // Affichage des rencontres d'un seul participant
                    System.out.printf("\n%s\n", dessinerLigne(110, '-'));                    
                    for (int i = 0; i < matches.length-1; i++)
                    {
                        for (int j = 0; j < matches[idEquipe].length; j++)
                        {
                            if (matches[idEquipe][j] == i+1)
                            {                                
                                System.out.printf("%-35s\n", String.format("%s vs %s", equipes[idEquipe], equipes[j]));
                                System.out.printf("%s\n", dessinerLigne(110, '-'));
                            }
                        }
                    }                    
                    break;
                
                case 4:
                    // Quitte le programme
                    continuer = false;
                    break;                    
                   
                default:
                    System.out.print("Choix invalide.\n");
                    break;
                           
            }
            
            if (choix != 4)    
            {
                Console.readLine("\nAppuyez sur entrée pour retourner au menu ...");   
                System.out.print("\n\n");
            }
        }       
    }    
    
    public static int nombreAleatoire(int inf, int sup)
    {
        return (int)(Math.random() * (sup + 1 - inf) + inf);
    }
    
    public static String dessinerLigne(int longueur, char symbole)
    {
        String ligne = "";
        for (int i = 0; i < longueur; i++)
            ligne += symbole;
        
        return ligne;
    }
    
    public static int indexParticipant(String participant, String[] equipes)
    {
        for (int i = 0; i < equipes.length; i++)
        {
            if (participant.equals(equipes[i]))
                return i;
        }
        
        return -1;
    }
  
}
