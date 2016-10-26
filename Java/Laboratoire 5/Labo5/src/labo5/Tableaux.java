package labo5;

public class Tableaux
{
    
    
    public static void decalerAGauche(int[] tableau)
    {
        int last = tableau[tableau.length-1];        
   
        for (int i = tableau.length-1; i > 0; i--)        
            tableau[i] = tableau[i-1];        
        
        tableau[0] = last;
    }
    
    public static void permuter(int[] tableau, int i, int j)
    {
        int temp = tableau[i];
        tableau[i] = tableau[j];
        tableau[j] = temp;
    }
    
    public static void permuter(String[] tableau, int i, int j)
    {
        String temp = tableau[i];
        tableau[i] = tableau[j];
        tableau[j] = temp;
    }
    
    public static int[][] genererRencontres(int nbEquipes)
    {
        int[][] rencontres = new int[nbEquipes][nbEquipes];        
        int[] equipes = new int[nbEquipes];
        
        // Initialisation tu tableau equipes
        for (int i = 0; i < equipes.length; i++)
            equipes[i] = i;
        
        // Création du tableau rencontres
        for (int i = 0; i < nbEquipes-1; i++)
        {
            decalerAGauche(equipes);
            permuter(equipes, 0, 1);
            
            for (int j = 0; j < nbEquipes; j++)            
                rencontres[equipes[nbEquipes-j-1]][equipes[j]] = i+1;                
        }
        
        return rencontres;
    }
   
}
