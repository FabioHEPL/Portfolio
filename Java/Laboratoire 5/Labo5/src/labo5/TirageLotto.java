package labo5;

import nhpack.Console;
import java.util.Random;

public class TirageLotto
{
    public static void main(String[] args)
    {
        int LONGUEUR = 7;
        
        int[] nombresUtilisateur = new int[] {1, 5, 8, 14, 20, 32, 42};
        int[] nombresLotto = new int[LONGUEUR];
        
        System.out.print("Bienvenue au tirage Lotto !\n\n");
        
        // Affichage du menu
        boolean jouer = true;
        while (jouer)
        {
            System.out.println("---------- MENU ----------");
            System.out.println("1. Tirage des nombres");
            System.out.println("2. Vérifier les nombres tirés avec ceux du joueur");
            System.out.println("3. Quitter le programme");
            System.out.print("--------------------------\n\n");

            char choix = Console.readLine("Votre choix : ").charAt(0);

            switch (choix)
            {
                case '1':
                    nombresLotto = genererTirageUnique(LONGUEUR);
                    System.out.print("Tirage effectué !");
                    break;

                case '2':
                    System.out.printf("Vous avez devinés %s nombre(s) !",
                            calculerNombreElementsCommuns(nombresLotto, nombresUtilisateur));
                    break;

                case '3':
                    jouer = false;
                    break;
            }
            
            System.out.println();
            afficherTableau(nombresUtilisateur);
            afficherTableau(nombresLotto);
            
            System.out.print("\n\n");
        }
        
        
    }
    
    public static int[] genererTirageUnique(int longueur)
    {
        Random random = new Random();
        
        int[] nombres = new int[longueur];       
        for (int i = 0; i < longueur; i++)
        {
            int nombreAleatoire;
            
            do
            {
                nombreAleatoire = random.nextInt(42) + 1;
            }
            while (numeroDejaTire(nombres, nombreAleatoire));
            
            nombres[i] = nombreAleatoire;            
        }
        
        return nombres; 
    }
    
    public static boolean numeroDejaTire(int[] tirage, int numero)
    {
        for (int i = 0; i < tirage.length; i++)
        {
            if (numero == tirage[i])
                return true;
        }
        
        return false;
    }
    
    public static int calculerNombreElementsCommuns(int[] tableau1, int[] tableau2)
    {
        int nombresCommuns = 0;
        
        for (int i = 0; i < tableau1.length; i++)
        {
            for (int j = 0; j < tableau2.length; j++)
            {
                if (tableau1[i] == tableau2[j])
                {
                    nombresCommuns++;
                }
            }
        }
        
        return nombresCommuns;        
    }
    
    public static void afficherTableau(int[] tableau)
    {
        for (int i = 0; i < tableau.length; i++)
        {
            System.out.print(tableau[i] + " ");            
        }
        
        System.out.println();
    }
}
