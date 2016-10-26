<?php session_start() ?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Light Poster :: Accueil</title>
    <link rel="stylesheet" href="styles/style.css">
</head>

<body>
    
    <?php
        include("header.php");
        include("autoload.php");
    ?>
        
    <section id="panier">
	
	    <div class="section-title">
		    <h1 class="title">Panier</h1>
	    </div>
    
        
        <?php
        
        include("secret/pswd.php");        
        $db = new mysqli("$host", "$user", "$password", "$user"."_db");       
        
        $productsManager = new ProductsManager($db);
        
        $panier = unserialize($_SESSION["client"]["panier"]);
        
        
        
        $products = $panier->getProducts($productsManager);
        
        if (count($products) == 0) {
            echo "<p class='confirmation-message'>Votre panier est vide.</p>";
        }
        else {     
            // Affiche la table du panier
            echo "<table id='shopping-card'>";
        
            echo "<tr>
                    <th>image</th>
                    <th>nom du produit</th>
                    <th>dimensions</th>
                    <th>quantité</th>
                    <th>supprimer</th>
                    <th>prix unitaire</th>                   
                    <th>total</th>
                  </tr>";
            
            $total = 0;
            foreach ($products as $product) {
                echo "<tr>";
                printf("<td class='product-td-image'><img src=%s /></td>", $product->image());
                printf("<td class='product-td-info'>%s</td>", $product->name());
                printf("<td class='product-td-size'>%s x %s</td>", $product->width(), $product->height());
            
                printf("<td class='product-td-quantity'>%s<br />", $product->quantity());
                echo "<td class='product-td-delete'><form id='product-form' action='panier.php' method='POST'>";
                echo "<input type='submit' value='Supprimer' name='supprimer' class='envoyer' /></td>";
                printf("<input type='hidden' name='code_article' value='%s'>", $product->code());
                echo "</form></td>";
                        
                printf("<td class='product-td-price'>%s €</td>", $product->price());
                printf("<td class='product-td-subtotal'>%s €</td>", $product->price() * $product->quantity());
                echo "</tr>";
                
                $total += $product->price() * $product->quantity();
            }
            
            printf("<tr><td colspan='6' class='product-td-total'>TOTAL : <td>%s €</td></td></tr>", $total);
                
            echo "</table>";
        }
        
        $_SESSION["client"]["panier"] = serialize($panier);        
        


        
        ?>
    
    
    </section>
    

        
    
</body>

</html>
