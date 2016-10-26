<?php session_start(); ?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Light Poster • Magasin</title>
    <link rel="stylesheet" href="styles/style.css" />
    <link rel="stylesheet" href="styles/scrollbar.css" />  
</head>

<body>

<?php 

include("uimenu.php");

?>

<div id="pagebody">

	<div id="section-title">
		<p>Magasin</p>
	</div>
	
    
    
	<?php
	
	afficherArticles();
    
    ?>
    
</div>

<script src="js/jquery.js"></script>
<script src="js/window_fix.js"></script>
<script src="js/center.js"></script>
<script src="js/outils.js"></script>
<script src="js/shopbuy.js"></script>
<script src="js/scrollbar.js"></script>


<?php
    
if (isset($_SESSION["client"])) {        
    echo '<script src="js/disconnect.js"></script>'; 
}
else {
    echo '<script src="js/login.js"></script>'; 
}
    
?>

</body>

</html>


<?php

function afficherArticles() {    
    include("secret/pswd.php");
	include("autoload.php");
	
    // Création d'une instance de la classe "ProductManager" pour pouvoir accèder facilement
    // aux articles dans la BD
	$db = new mysqli("$host", "$user", "$password", "$user"."_db");
	$productsManager = new ProductsManager($db);
	
	$products = $productsManager->getAllProducts();

    
    // Afficher les articles
	echo "<ul>";		

	foreach ($products as $product) {				 
		echo "<li class='product-list'>";				
		echo "<div class='product'>";
		echo "<ul class='product-info'>";
			
		printf("<li class='product-info-image'><span class='helper'></span><img src='%s' /></li>", $product->image());      
		printf("<li class='product-info-name'>%s</li>", $product->name());
		printf("<li class='product-info-size'>%s x %s cm</li>", $product->width(), $product->height());
		printf("<li class='product-info-price'>%s €</li>", $product->price());
				   
		echo "<form id='product-form'>";
		echo "<li class='product-info-setquantity'><span class='quantity-label'>Quantité : </span><input type='text' class='quantity-field' name='quantite' value='1' required></li>";
		echo "<li class='product-info-buybutton'><span class='buybgap'></span><button type='button' name='achat' class='buyproduct-button'>Ajouter au panier</button></li>";
		printf("<input type='hidden' name='code_article' value='%s'>", $product->code());
		echo "</form>";				
			 
		echo "</ul>";
		echo "</div>";
			
		echo "</li>";
	}
    
	echo "</ul>";
}

?>
