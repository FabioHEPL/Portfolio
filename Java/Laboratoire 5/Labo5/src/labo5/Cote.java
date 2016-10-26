/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package labo5;

public class Cote
{
    public static void main(String[] args)
    {
        System.out.println(trouverGrade(80.0f));
    }
    
    public static char trouverGrade(float coteMoyenne)
    {
        char[] grades = {'A', 'B', 'C', 'D', 'F'};
        float[] limites = {90.0f, 80.0f, 70.0f, 60.0f, 0.0f};
        char resultat = '?';
                
        for (int i = 0; i < limites.length && resultat == '?'; ++i)
        {
            if (coteMoyenne >= limites[i])
            {
                resultat = grades[i];
            }
        }
        return resultat;
    }
}
