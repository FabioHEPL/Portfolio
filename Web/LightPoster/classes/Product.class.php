<?php

/**
 * Item short summary.
 *
 * Item description.
 *
 * @version 1.0
 * @author Fabio
 */
class Product
{
    private $_id;
    private $_code;
    private $_name;
    private $_price;
    private $_width;
    private $_height;
    private $_category;
    private $_image;   
    private $_quantity;
    
    // CONSTRUCT
    public function __construct(array $data) {
        $this->hydrate($data);    
    }
    
    public function hydrate(array $data) {
        
        foreach ($data as $key => $value)
        {
            $method = "set".ucfirst($key);
            
            if (method_exists($this, $method))
            {
                $this->$method($value);            
            }        
        }    
    }    
    
    // GETTERS
    public function id() {
        return $this->_id;
    }
    
    public function code() {
        return $this->_code;
    }
    
    public function name() {
        return $this->_name;
    }
    
    public function price() {
        return $this->_price;
    }
    
    public function width() {
        return $this->_width;
    }
    
    public function height() {
        return $this->_height;
    }
	
	public function category() {
        return $this->_category;
    }
    
    public function image() {
        return $this->_image;
    }
    
    public function quantity() {
        return $this->_quantity;
    }
    
    // SETTERS
    public function setID($id) {
        $this->_id = $id;
    }
    
    public function setCode($code) {
        $this->_code = $code;
    }
    
    public function setName($name) {
        $this->_name = $name;
    }    
    
    public function setPrice($price) {
        $this->_price = $price;
    }
        
    public function setWidth($width) {
        $this->_width = $width;
    }
    
    public function setHeight($height) {
        $this->_height = $height;
    }
    
    public function setCategory($category) {
        $this->_category = $category;
    }
    
    public function setImage($image) {
        $this->_image = $image;
    }
    
    public function setQuantity($quantity) {
        $this->_quantity = $quantity;
    }
    
    // METHODS
    public function show() {

	}
}

?>
