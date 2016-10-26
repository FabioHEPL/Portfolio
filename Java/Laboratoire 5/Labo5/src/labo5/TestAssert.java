package labo5;

public class TestAssert
{
    public static void main(String[] args)
    {     
        
        String chaine =  "ikilledagoat";
        System.out.println(chaine.substring(4));
        System.out.println(chaine.substring(1, 5));
        
    }
        
    public static char lettre(int numero)
    {        
        switch (numero)
        {
            case 1:
                return 'A';                
            
            case 2:
                return 'B';
            
            case 3:
                return 'C';
            
            default:
                return 'Z';
                
        }        
    }
    
    public static int nombreAleatoire()
    {
        return 3;
    }
}


    // 


