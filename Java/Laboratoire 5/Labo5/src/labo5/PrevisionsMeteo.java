package labo5;

import nhpack.Console;

public class PrevisionsMeteo
{
    public static void main(String args[])
    {
        float[][] temperatures = new float[2][3];            
        for (int i = 0; i < temperatures.length; i++)        
            encoderReleves(i, temperatures[i]);        
        
        float[] moyenne = new float[temperatures.length];        
        for (int i = 0; i < moyenne.length; i++)       
            moyenne[i] = moyenneColonne(i, temperatures);
        
        System.out.print("\n");                
        
        
        // Affichage du tableau
        // 1. Affichage de l'en-tête
        System.out.printf("%15s", "");
        for (int i = 0; i < temperatures.length; i++)        
            System.out.printf("%-15s", getLibelleLieu(i));        
        
        System.out.print("\n");
        
        
        // 2. Affichage contenu
        for (int i = 0; i < temperatures[0].length; i++)
        {
            System.out.printf("%-15s", getLibelleJour(i));
            for (int j = 0; j < temperatures.length; j++)            
                System.out.printf("%-15.2f", temperatures[j][i]);            
            
            System.out.print("\n");
        }
        
        
        // 3. Affichage moyenne
        System.out.printf("\n%-15s", "MOYENNE");            
        for (int i = 0; i < moyenne.length; i++)        
            System.out.printf("%-15.2f", moyenne[i]);        
        
        System.out.print("\n");
    }
    
    public static void encoderReleves(int indiceLieu, float ligne[])
    {
        for (int i = 0; i < 3; i++)
        {
            System.out.printf("Encodez la temperature de %s pour %s : ",
                    getLibelleLieu(indiceLieu), getLibelleJour(i));
            
            ligne[i] = Float.parseFloat(Console.readLine()); 
        }
    }
    
    public static String getLibelleLieu(int indiceLieu)
    {
        switch (indiceLieu)
        {
            case 0:
                return "Anvers";
            
            case 1:
                return "Bruxelles";
                
            case 2:
                return "Dinant";
            
            case 3:
                return "Ostende";
                
            case 4:
                return "Verviers";
            
            default:
                return "";
        }        
    }
    
    public static String getLibelleJour(int indiceJour)
    {
        switch (indiceJour)
        {
            case 0:
                return "Lundi";
            
            case 1:
                return "Mardi";
                
            case 2:
                return "Mercredi";
            
            case 3:
                return "Jeudi";
                
            case 4:
                return "Vendredi";
            
            case 5:
                return "Samedi";
                
            case 6:
                return "Dimanche";
                
            default:
                return "";
        }      
    }
    
    

    
    public static void afficherLigne(int indiceJour, float[] tableau)
    {
        System.out.printf("%-15s", getLibelleJour(indiceJour));
        
        for (int i = 0; i < tableau.length; i++)        
            System.out.printf("%-15.2f", tableau[i]);
                
        System.out.print("\n");
    }
    
    
    public static float moyenneColonne(int indiceLieu, float tableau[][])
    {
        float somme = 0;
        for (int i = 0; i < tableau[indiceLieu].length; i++)        
            somme += tableau[indiceLieu][i];       
        
        return somme / tableau[indiceLieu].length;
    }
    
   
    
    
    
    
    
    
    
    
    
}
