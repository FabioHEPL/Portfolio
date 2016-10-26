package pongs;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Raquette
{
    private float x;
    private float y;
    private float largeur;
    private float hauteur;
    private Color couleur;
    private Vecteur direction;
        
    public Raquette(float largeur, float hauteur)
    {
        x = 0f;
        y = 0f;
        
        this.largeur = largeur;
        this.hauteur = hauteur;
        
        couleur = Color.BLUEVIOLET;
        
        direction = new Vecteur(0, 1);
    }
    
    public void SetPosition(float x, float y)
    {
        this.x = x;
        this.y = y;
    }    
    
    public void deplacer(float vitesse)
    {
        x += direction.getX() * vitesse;
        y += direction.getY() * vitesse;        
    }
    
    public void inverserDirectionX()
    {
        direction.setX(-direction.getX());
    }
    
    public void inverserDirectionY()
    {
        direction.setY(-direction.getY());
    }
    
    public void dessiner(GraphicsContext peintre)
    {
        peintre.setFill(this.couleur);
        peintre.fillRect(x, y, largeur, hauteur);
    }   
    
    public void SetColor(Color couleur)
    {
        this.couleur = couleur;
    }
     
    public float getX() { return this.x; }
    public float getY() { return this.y; }
    public float getLargeur() { return this.largeur; }
    public float getHauteur() { return this.hauteur; }
}
