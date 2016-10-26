package pongs;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class JeuPong
{
    private Balle balle = null;
    private Raquette raquetteA = null;
    private Raquette raquetteB = null;
    //private Raquette joueur1 = null;
    //private Raquette joueur2 = null;
    
    public JeuPong()
    {
        balle = new Balle();
        
        raquetteA = new Raquette(8, 150);           
        raquetteA.SetPosition(0, 0);        
        raquetteA.SetColor(Color.BLUEVIOLET);
        
        raquetteB = new Raquette(8, 150);    
        raquetteB.SetPosition(Programme.LARGEUR_EN_PIXEL - raquetteB.getLargeur(), 0);
        raquetteB.SetColor(Color.CORNFLOWERBLUE);
    }
    
   /** La méthode mettre à jour contiendra la logique du jeu Pong.
    *  Elle définit notamment les interactions entre la balle et les élements du jeu.
    *  La méthode est appelée toute les 30 secondes.
    */
   public void mettreAJour()
   {
        // Vérifier collisions
        Bords bordCollision = checkCollisions();
        if (bordCollision != null)
        {
            if (bordCollision == Bords.Haut || bordCollision == Bords.Bas)
                // On inverse la direction verticale
                balle.inverserDirectionY();
            else
                // On inverse la direction horizontale
                balle.inverserDirectionX();
        }
        
        // Déplacer la balle
        balle.deplacer(10f);
        raquetteA.deplacer(2f);
        raquetteB.deplacer(2f);
    }
   
   /** La méthode dessinerScene fait le rendu de la scène à l'écran.
    *  La méthode est appelée par le nhpack toutes les trente secondes et lui
    *  passe en paramètre l'objet responsable des dessins.
    */
   public void dessinerScene(GraphicsContext peintre)
   {
       mettreAJour();
       peintre.setFill(Color.WHITE);
       peintre.fillRect(0, 0, Programme.LARGEUR_EN_PIXEL, Programme.HAUTEUR_EN_PIXEL);
        
       // Dessiner la balle
       balle.dessiner(peintre);
       raquetteA.dessiner(peintre);
       raquetteB.dessiner(peintre);
   }
   
   public Bords checkCollisions()
   {
        if (balle.getY() - balle.getRayon() <= 0)
           return Bords.Haut;
       
        else if (balle.getX() + balle.getRayon() >= Programme.LARGEUR_EN_PIXEL)
            return Bords.Droite;

        else if (balle.getY() + balle.getRayon() >= Programme.HAUTEUR_EN_PIXEL)
            return Bords.Bas;

        else if (balle.getX() - balle.getRayon() <= 0)
            return Bords.Gauche;
      
       return null;
   }
   
   public enum Bords 
   {
      Haut,
      Droite,
      Bas,
      Gauche
   }           
}
