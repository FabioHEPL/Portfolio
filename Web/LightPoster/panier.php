<?php session_start(); ?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Light Poster • Votre Panier</title>
    <link rel="stylesheet" href="styles/style.css" />
    <link rel="stylesheet" href="styles/scrollbar.css" />  
</head>

<body>

<?php
    
if (isset($_SESSION["client"])) {        
    echo '<script src="js/disconnect.js"></script>'; 
}
else {
    echo '<script src="js/login.js"></script>'; 
}
    
?>

<?php 

include("uimenu.php");

?>

<div id="pagebody">
	<div id="section-title">
		<p>Panier</p>
	</div>
		
	<?php
	
	afficherPanier();
    
    afficherInfosClient();
    
    
    ?>
    
    
    
</div>

<script src="js/jquery.js"></script>
<script src="js/window_fix.js"></script>
<script src="js/center.js"></script>
<script src="js/outils.js"></script>
<script src="js/shoppingcard.js"></script>
<script src="js/scrollbar.js"></script>

<script>

    


</script>




</body>

</html>


<?php

function afficherPanier() {      
    include("secret/pswd.php");
	include("autoload.php");   
    
    $db = new mysqli("$host", "$user", "$password", "$user"."_db");             
    $productsManager = new ProductsManager($db);
    
    $panier = unserialize($_SESSION["client"]["panier"]);        
        
    $products = $panier->getProducts($productsManager);
        
    if (count($products) == 0) {
        echo "<p class='shoppingcardempty-message'>Votre panier est vide.</p>";
    }
    else {     
        // Affiche la table du panier
        echo "<table id='shopping-card'>";
        
        echo "<tr>
                <th>image</th>
                <th>nom du produit</th>
                <th>dimensions</th>
                <th>quantité</th>
                <th>modifier</th>
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
            
            echo "<td class='product-td-modify'>";
            
            printf("<span class='quantity-label'>Quantité : </span><input type='text' class='quantity-field' name='quantite' value='%s'", $product->quantity());
            echo "<br /><br /><button type='button' name='modifier' class='modifyproduct'>Modifier</button>";
            
            echo "</td>";
            
            echo "<td class='product-td-delete'><form id='product-form'>";
            echo "<button type='button' name='supprimer' class='deleteproduct'>Supprimer</button>";
            printf("<input type='hidden' name='code_article' value='%s'>", $product->code());
            echo "</form></td>";
            
            
                        
            printf("<td class='product-td-price'>%s €</td>", $product->price());
            printf("<td class='product-td-subtotal'>%s €</td>", $product->price() * $product->quantity());
            echo "</tr>";
            
            
                
            $total += $product->price() * $product->quantity();
        }
            
        printf("<tr><td colspan='7' class='product-td-total'>TOTAL : </td><td class='product-td-total-num'>%s €</td></tr>", $total);
                
        echo "</table>";
    }
        
    $_SESSION["client"]["panier"] = serialize($panier);
 }

 
 function afficherInfosClient() {
    include("secret/pswd.php");
    $db = new mysqli("$host", "$user", "$password", "$user"."_db"); 
    
    $k = sprintf("SELECT pseudo,email,adresse,telephone FROM clients WHERE pseudo LIKE '%s'", $_SESSION["client"]["pseudo"]);
    

    $result = $db->query($k);
    
    print("<div id='infos-client'>");
    
    while ($row = $result->fetch_assoc()) {
        
        printf("Pseudo : %s<br />", $row["pseudo"]);
        printf("Email : %s<br />", $row["email"]);
        printf("Adresse : %s<br />", $row["adresse"]);
        printf("Telephone : %s<br />", $row["telephone"]);
    }
    
    print("</div>");
    
    $db->close();
 }