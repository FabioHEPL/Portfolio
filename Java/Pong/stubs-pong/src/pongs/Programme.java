package pongs;

import nhpack.Console;
import nhpack.SceneBuilderFactory;


public class Programme
{
    public static final int HAUTEUR_EN_PIXEL = 600;
    public static final int LARGEUR_EN_PIXEL = 800;
    
    public static void main(String[] args)
    {
        JeuPong pong = new JeuPong();

        SceneBuilderFactory.newInstance()
                .withDimension(LARGEUR_EN_PIXEL, HAUTEUR_EN_PIXEL)
                .withDrawMethod(pong::dessinerScene)
                .finish();
    }
    
}
