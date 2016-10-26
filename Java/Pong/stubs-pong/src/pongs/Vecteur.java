package pongs;

public class Vecteur
{
    private float x;
    private float y;
    
    public Vecteur(float x, float y)
    {
        this.x = x;
        this.y = y;
    }
    
    public void set(float x, float y)
    {
        this.x = x;
        this.y = y;
    }
    
    public void setX(float x) { this.x = x; }
    public void setY(float y) { this.y = y; }
    public float getX() { return x; }
    public float getY() { return y; }
    
    public void normaliser()
    {
        float longueur = (float) Math.sqrt(x*x + y*y);      
        
        if (longueur != 0)  
        {
            x = x / longueur;
            y = y / longueur;
        }   
    }
    
    public boolean equals(float x, float y)
    {
        if (this.x == x && this.y == y)
            return true;
        else
            return false;
    }
    

}
