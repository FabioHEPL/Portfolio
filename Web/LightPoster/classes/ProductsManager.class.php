<?php

/**
 * ItemsManager short summary.
 *
 * ItemsManager description.
 *
 * @version 1.0
 * @author Fabio
 */
class ProductsManager
{
    private $_db;
    
    private $_fieldName;
    
    public function __construct($db)
    {
        $this->setDB($db);
        $this->_db->query("SET NAMES 'utf8'");
        $this->_fieldName = array("id", "code", "name", "price", "width", "height", "category", "image", "quantity");
    } 
    
    function __destruct() {
        $this->_db->close();
    }
    
    public function setDB($db) {
        $this->_db = $db;
    }
    
    public function getList() {
		
	} 
    
    public function getProductQuantity($productCode) {
        $result = $this->_db->query("SELECT quantite from articles WHERE code_article LIKE '$productCode'");
        
        $row = $result->fetch_row();
        
        return $row[0];
    }
	
	public function getProduct($productCode) {
		$result = $this->_db->query("SELECT * from articles WHERE code_article LIKE '$productCode'");
		
        $row = $result->fetch_row();        
        
        $data = array();
        for ($i = 0; $i < count($row); $i++) {
            $data[$this->_fieldName[$i]] = $row[$i];
        }          
       
        return new Product($data);		
	}
        
    public function getAllProducts() {
		$result = $this->_db->query("SELECT * from articles");
		
		$products = array();
       
		while ($row = $result->fetch_row()) {
            $data = array();
            
            for ($i = 0; $i < count($row); $i++) {
                $data[$this->_fieldName[$i]] = $row[$i];
            }
            
            $products[] = new Product($data);           
        }        
        return $products;		
	}   
    
    public function changeProductQuantity($productCode, $quantity) {
        $this->_db->query("UPDATE articles SET quantite = '$quantity' WHERE code_article LIKE '$productCode'");
    }
    
    public function updateProductQuantity($productCode, $quantity) {
        $this->_db->query("UPDATE articles SET quantite = quantite + '$quantity' WHERE code_article LIKE '$productCode'");
    }
}
