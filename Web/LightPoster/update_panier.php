<?php

session_start();

include("secret/pswd.php");
include("autoload.php");    


if (! isset($_POST["action"])) {
    exit();
}
else {
    print("action post !");
}


    
$action = $_POST["action"];
$returnData = array();


switch ($action) {
    case "ok" :
        print("action = ok");
        print($_POST["ytest"]);
        break;
    // Ajouter un article au panier
    case "achat":
        // Variables post envoyées :
        // "code_article" : le code de l'article qu'on veut acheter
        // "quantite" : quantité d'articles du même type qu'on veut acheter   

        // Si l'utilisateur n'est pas connecté ...
        if (! isset($_SESSION["client"]["panier"])) {
            $returnData["message"] = "NotConnected";
            echo json_encode($returnData);	
        }
        // Si l'utilisateur est déjà connecté au site, ajouter l'article au panier
        else {  
            // Achat de l'article
            $db = new mysqli("$host", "$user", "$password", "$user"."_db");
            $productsManager = new ProductsManager($db);
            $panier = unserialize($_SESSION["client"]["panier"]);

            $codeArticle = $_POST["code_article"];
            $quantiteArticle = $_POST["quantite"] + $panier->getProductQuantity($codeArticle);	
	
            $quantiteEnStock = $productsManager->getProductQuantity($codeArticle);
	
            if ($quantiteArticle > $quantiteEnStock) {
                $returnData["message"] = "QuantityExceed";
                $returnData["availableQuantity"] = $quantiteEnStock;
                $returnData["chosenQuantity"] = $quantiteArticle; 
        
                echo json_encode($returnData);
            }
            else {
                // Ajouter l'article au panier
                $panier->add($codeArticle, $_POST["quantite"]);
                $_SESSION["client"]["panier"] = serialize($panier);
    
                $returnData["message"] = "SuccessfulPurchase";
                echo json_encode($returnData);
            }	
        }
        
        break;
  
            
    // Enlèver un article du panier
    case "remove":
        $codeArticle = $_POST["code_article"];    
        
        $panier = unserialize($_SESSION["client"]["panier"]);
        $panier->remove($codeArticle);
        $_SESSION["client"]["panier"] = serialize($panier);  
        
        $returnData["message"] = "SuccessfulRemove";
        echo json_encode($returnData);        
        
        break;
        
    
        
    case "modifier":
        // Modifier la quantité d'un article
        $db = new mysqli("$host", "$user", "$password", "$user"."_db");
        $productsManager = new ProductsManager($db);
        $panier = unserialize($_SESSION["client"]["panier"]);

        $codeArticle = $_POST["code_article"];
        $quantiteArticle = $_POST["quantite"];	
	
        $quantiteEnStock = $productsManager->getProductQuantity($codeArticle);
	
        if ($quantiteArticle > $quantiteEnStock) {
            $returnData["message"] = "QuantityExceed";
            $returnData["availableQuantity"] = $quantiteEnStock;
            $returnData["chosenQuantity"] = $quantiteArticle;
        
            echo json_encode($returnData);
        }
        else {
            // Ajouter l'article au panier
            $panier->modifyQuantity($codeArticle, $quantiteArticle);
            $_SESSION["client"]["panier"] = serialize($panier);
    
            $returnData["message"] = "SuccessfulEdit";
            $returnData["chosenQuantity"] = $quantiteArticle;
            
            echo json_encode($returnData);    
        }
        
        break;
    
    
}

?>
