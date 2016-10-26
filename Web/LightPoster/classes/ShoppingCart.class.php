<?php

/**
 * ShoppingCart short summary.
 *
 * ShoppingCart description.
 *
 * @version 1.0
 * @author Fabio
 */
class ShoppingCart
{
    private $_products;    
    
    // CONSTRUCT
    public function __construct(array $products = array()) {
        $this->_products = $products;
    }
    
    // Ajoute un article au panier
    public function add($productCode, $quantity) {
		// Vérifie si l'article est déjà dans le panier
        $productPos = $this->findProduct($productCode);
		
		// Si la position est égale à -1, l'article n'est pas présent dans le panier
        if ($productPos == -1) {
		    $this->_products[] = array("product_code" => $productCode, "quantity" => $quantity);
	    }
        else {
            $this->_products[$productPos]["quantity"] += $quantity;
        }
    }
    
    public function modifyQuantity($productCode, $quantity) {
		$productPos = $this->findProduct($productCode);
		
		$this->_products[$productPos]["quantity"] = $quantity;		
	}
    
    
    public function remove($productCode) {
        for ($i = 0; $i < count($this->_products); $i++) {
            if ($this->_products[$i]["product_code"] == $productCode) {
                unset($this->_products[$i]);
                $this->_products = array_values($this->_products);
                return;
            }
        }        
    }
    
    
    public function getProductQuantity($productCode) {
        for ($i = 0; $i < count($this->_products); $i++) {
            if ($this->_products[$i]["product_code"] == $productCode) {
                return $this->_products[$i]["quantity"];               
            }         
        }
        return 0;
    }
    
    
    
    public function findProduct($productCode) {
        for ($i = 0; $i < count($this->_products); $i++) {
            if ($this->_products[$i]["product_code"] == $productCode) {
                return $i;               
            }         
        }    
        return -1;
    }
    
    public function getProducts($productsManager) {
        $products = array();
        foreach ($this->_products as $product) {
            $tmp = $productsManager->getProduct($product["product_code"]);
            $tmp->setQuantity($product["quantity"]);
                    
            array_push($products, $tmp);            
        }
        
        return $products;
    }
    
    public function countProducts() {
        return count($this->_products);
    }
    
    
    public function printDebug() {
        print("Panier :<br /><br />");
        for ($i = 0; $i < count($this->_products); $i++) {
            printf("%s) Code: %s | Quantity : %s<br />", $i, $this->_products[$i]["product_code"], $this->_products[$i]["quantity"]);
        }
    }   

}

?>
