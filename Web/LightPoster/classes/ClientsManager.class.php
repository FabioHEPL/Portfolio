<?php

/**
 * ClientManager short summary.
 *
 * ClientManager description.
 *
 * @version 1.0
 * @author Fabio
 */
class ClientsManager
{
    private $_db;
    
    public function __construct($db)
    {
        $this->setDB($db);
        $this->_db->query("SET NAMES 'utf8'");
    }
    
    function __destruct() {
        $this->_db->close();
    }
    
    public function setDB($db) {
        $this->_db = $db;
    }
    
    // Ajoute un client à la table "clients"
    public function add(Client $client) {
       $nickname = $client->nickname();
       $password = md5($client->password());
       $email = $client->email();
       $adress = $client->adress();
       $telephoneNumber = $client->telephoneNumber();       
    
       $this->_db->query("INSERT INTO clients VALUES ('', '$nickname', '$password', '$email', '$adress', '$telephoneNumber')");       
    }
    
    // Vérifie si un client avec le même pseudo est déjà présent dans la table
    public function isUserInDB($nickname) {
        $result = $this->_db->query("SELECT pseudo FROM clients WHERE pseudo LIKE '$nickname'");
        
        if ($result->num_rows > 0)
            return true;     
        else 
            return false;        
    }
    
    public function checkPassword($nickname, $password) {
        $result = $this->_db->query("SELECT mdp FROM clients WHERE pseudo LIKE '$nickname'");
       
		$field = $result->fetch_row();
		$passwordBD = $field[0];
       
        if ($password == $passwordBD) 
            return true;
        else
            return false;       
    }
}
