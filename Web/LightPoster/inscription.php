<?php

session_start();

include("secret/pswd.php");
include("autoload.php");
    
$data = array (
    "nickname" => $_POST["pseudo"],
    "password" => $_POST["mdp"],
    "adress" => $_POST["adresse"],
    "telephoneNumber" => $_POST["telephone"]
);
        
$db = new mysqli("$host", "$user", "$password", "$user"."_db");
        
$clientsManager = new ClientsManager($db);
        
// Vérifier si le pseudo existe déjà
if ($clientsManager->isUserInDB($data["nickname"])) {
    echo "1";
        
}
else {
    $clientsManager->add(new Client($data));                
    echo "2";  
} 


?>