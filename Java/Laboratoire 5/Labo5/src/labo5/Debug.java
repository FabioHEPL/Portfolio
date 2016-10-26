package labo5;

public class Debug
{
    public static void afficherTableau(String[] tab)
    {
        for (int i = 0; i < tab.length; i++)        
            System.out.printf("%s ", tab[i]);
                
        System.out.print("\n");
    }
    
    public static void afficherTableau(int[] tab)
    {
        for (int i = 0; i < tab.length; i++)        
            System.out.printf("%s ", tab[i]);
                
        System.out.print("\n");
    }
    
    public static void afficherTableau(int[][] tab)
    {
        for (int i = 0; i < tab.length; i++)
        {
            for (int j = 0; j < tab[i].length; j++)            
                System.out.print(tab[i][j] + " ");            
            
            System.out.println();
        }
    }    
}
