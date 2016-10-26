import nhpack.Console;

public class Labo5Championnat {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        int choix,nombreParticipants;
        boolean menu=false;
        
        do
        {
            nombreParticipants=Integer.parseInt(Console.readLine("Combien de joueurs dans ce championnat ? "));
        }
        while (nombreParticipants%2!=0);

        String participants[]=new String[nombreParticipants];
        int[][] matchs = null;
        do
        {
            choix = choixMenu();
            switch (choix)
            { 
                case 1:
                    encoderListeParticipants(participants); 
                    melangerTableau(participants);
                    menu = true; 
                    break;
                case 2:
                   System.out.println("Voici la liste des participants : ");
                   afficherListeParticipants (participants);
                    menu=true;
                    break;
                case 3:
                    matchs = genererProchainMatch(participants);
                    for (int i = 0; i < matchs.length; i++) {
                        System.out.println(participants[matchs[i][0]] + " contre " + participants[matchs[i][1]]);
                    }
                    
                    /*matchsDeJournee(participants);
                    menu = true;*/
                    break;
                case 4:
                    String nomEquipe = Console.readLine("Nom equipe : ");
                    
                    int IDEquipe = 0;
                   
                    for (int i = 0; i < participants.length-1; i++) {
                        matchs = genererProchainMatch(participants);
                        
                        for (int k=0; k<participants.length; k++) {
                            if (participants[k].equals(nomEquipe))
                                IDEquipe = k;
                        }
                        
                        for (int j = 0; j < matchs.length; j++) {
                            if (matchs[j][0] == IDEquipe){
                                System.out.println(participants[matchs[j][0]] + " contre " + participants[matchs[j][1]]);
                            }
                            else if (matchs[j][1] == IDEquipe) {
                                System.out.println(participants[matchs[j][1]] + " contre " + participants[matchs[j][0]]);
                            }
                        }
                    }
                    
                    
                    break;
                case 5:
                    System.out.println ("Au revoir.");
                    // fermeture du menu 
                    menu = false;
                    break;
            }
        } 
        while (menu == true);
    }
        
    
    public static int choixMenu()
    {
        String reponse = "";
        int monChoix;
        char choix;
        int choixUtile;
        
        do 
        {            
            System.out.println("1. Veuillez entrer la liste des participants");
            System.out.println("2. Afficher les liste des participants");
            System.out.println("3. Afficher les matchs d'une journée ");
            System.out.println("4. Afficher les matchs d'un participant");
            System.out.println("5. Quitter");

            reponse = Console.readLine("\nQuel est votre choix : ");
            monChoix=Integer.parseInt(reponse);
            
            choix=reponse.charAt(0);
            if (choix != '1' && choix != '2' && choix != '3' && choix !='4' && choix !='5')
            {   System.out.println("Veuillez choisir un des 4 choix (1,2,3 ou 4)");
                Console.readLine();
            }
        }
        while(choix != '5' && choix != '4' && choix != '3' && choix != '2' && choix != '1');
        
        choixUtile=Integer.parseInt(reponse);       
        
        return choixUtile;
    }
    
    public static void encoderListeParticipants( String participants[])
    {
        for(int i=0;i<participants.length;i++)
            participants[i]=Console.readLine("Encodez le joueur  ");
    } 
    
    public static void afficherListeParticipants (String participants[])
    {
        for(int i=0;i<participants.length;i++)
            System.out.println(participants[i]);
        /*for (String membre : participants)
            System.out.println(membre);*/
    }
            
    public static void permuter(String[] tableau, int i, int j)
    {
        String temp = tableau[i]; tableau[i] = tableau[j];
        tableau[j] = temp;
    }
        
    public static int nbAleatoire(int inf, int sup)
    {
        return (int) (Math.random()*(sup + 1 - inf) + inf);
    }    
    
    
    public static void melangerTableau(String[] tableau)
    {
        for (int i = 0; i < tableau.length; i++) {
            int random = nbAleatoire(i, tableau.length-1);
            permuter(tableau, i, random);            
        }        
    }
    
    public static void decalerADroite(String[] tableau)
    {
        String tmp = tableau[0];       
        for (int i=0; i<tableau.length-1; i++) {
            tableau[i] =tableau[i + 1];
        }
        tableau[tableau.length-1] = tmp;
    }    
    
    
    public static int[][] genererProchainMatch(String[] tableau)
    {
        int[][] matchs = new int[tableau.length/2][2];
        
        decalerADroite(tableau);
        permuter(tableau, 0, 1);
               
        for (int i=0; i<tableau.length/2; i++){
            matchs[i][0] = i; matchs[i][1] = tableau.length-i-1;
        }    
        
        return matchs;
    }
}

