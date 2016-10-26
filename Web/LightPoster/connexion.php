<?php

header('Content-type: text/plain');
session_start();



include("secret/pswd.php");
include("autoload.php");    
    
$data = array (
    "nickname" => $_POST["pseudo"],
    "password" => $_POST["mdp"],
);
        
$db = new mysqli("$host", "$user", "$password", "$user"."_db");
        
$clientsManager = new ClientsManager($db);
        
// Vérifier si le pseudo existe
if (! $clientsManager->isUserInDB($data["nickname"])) {
    echo json_encode("Inexistant");        
}

// Si le pseudo existe, vérifier si le mot de passe est correct
else {
    if ($clientsManager->checkPassword($data["nickname"], md5($data["password"]))) {
    
        // Création du panier
    	include("secret/pswd.php");
	    include("autoload.php");
	
	    $db = new mysqli("$host", "$user", "$password", "$user"."_db");
	    $productsManager = new ProductsManager($db);
        
        $_SESSION["client"]["pseudo"] = $data["nickname"];     
		$_SESSION["client"]["panier"] = serialize(new ShoppingCart());	
        
        echo json_encode("Connecté");
    }
    else {
        echo json_encode("Mdp Incorrect");   
    }
} 

?>

