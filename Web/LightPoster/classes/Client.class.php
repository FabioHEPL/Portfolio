<?php

/**
 * Client short summary.
 *
 * Client description.
 *
 * @version 1.0
 * @author Fabio
 */
class Client
{
    private $_nickname;
    private $_password;
    private $_email;
    private $_adress;
    private $_telephoneNumber;
    
    
    // CONSTRUCT
    public function __construct(array $data) {
        $this->hydrate($data);    
    }
    
    public function hydrate(array $data) {        
        foreach ($data as $key => $value) {
            $method = "set".ucfirst($key);
            
            if (method_exists($this, $method)) {
                $this->$method($value);            
            }        
        }    
    }
        
    // GETTERS
    public function nickname() {
        return $this->_nickname;
    }
    
    public function password() {
        return $this->_password;
    }
    
    public function email() {
        return $this->_email;
    }
    
    public function adress() {
        return $this->_adress;
    }
    
    public function telephoneNumber() {
        return $this->_telephoneNumber;
    }

    
    // SETTERS
    public function setNickname($nickname) {
        $this->_nickname = $nickname;
    }
    
    public function setPassword($password) {
        $this->_password = $password;
    }    
    
    public function setEmail($email) {
        $this->_email = $email;
    }
        
    public function setAdress($adress) {
        $this->_adress = $adress;
    }
    
    public function setTelephoneNumber($telephoneNumber) {
        $this->_telephoneNumber = $telephoneNumber;
    }
}

?>
