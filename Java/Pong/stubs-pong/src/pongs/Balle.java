package pongs;
 
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Balle
{
    private float x;
    private float y;    
    private float rayon;
    private Vecteur direction;
    private Color couleur;
    private final static float[][] directionsInvalides = new float[][] {{-1f, 0f}, {1f, 0f},
                                                   {0f, 1f}, {0f, -1f}, {0f, 0f}};    
        
    // Constructeur
    public Balle()
    {
        x = Programme.LARGEUR_EN_PIXEL / 2f;
        y = Programme.HAUTEUR_EN_PIXEL / 2f;
        rayon = 15f;
        couleur = Color.ORANGE;
        
        this.setDirectionAleatoire();
    }
        
    // Getters
    public float getX() { return this.x; }
    public float getY() { return this.y; }
    public float getRayon() { return rayon; }
     
    // Setters
    public void setRayon(float rayon)
    { 
        if (rayon > 0f)
            this.rayon = rayon;
    };
    
    // Méthodes
    private void setDirectionAleatoire()
    {
        Vecteur direction = new Vecteur(nombreAleatoire(-1f, 1f), nombreAleatoire(-1f, 1f));          

        while (! isDirectionValide(direction))
            direction.set(nombreAleatoire(-1f, 1f), nombreAleatoire(-1f, 1f));
            
        this.direction = direction;
        this.direction.normaliser();
    }
        
    private boolean isDirectionValide(Vecteur direction)
    {
        for (int i = 0; i < Balle.directionsInvalides.length; i++)
        {
            if (direction.equals(Balle.directionsInvalides[i][0], Balle.directionsInvalides[i][1]))
                return false;
        }
        
        return true;
    }   
    
    public void inverserDirectionX()
    {
        direction.setX(-direction.getX());
    }
    
    public void inverserDirectionY()
    {
        direction.setY(-direction.getY());
    }
    
    
    public void deplacer(float vitesse)
    {           
        x += direction.getX() * vitesse;
        y += direction.getY() * vitesse;
    }
    
    public void dessiner(GraphicsContext peintre)
    {
        peintre.setFill(this.couleur);
        peintre.fillOval(x - rayon, y - rayon, rayon * 2, rayon * 2);
    }    
    
    private float nombreAleatoire(float min, float max)
    {
        return min + (float)Math.random() * (max - min);
    }
    
}