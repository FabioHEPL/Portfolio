<aside id="page-links-bar">    
    <div id="website-logo-wrap">
        <img src="./images/site/website_logo.png" />
    </div>

  	<ul>
        <li class="page-link">
            <a>Accueil</a>
            <img src="./images/site/icones/accueil.png" />
        </li>
        <li class="page-link">
            <a href="./magasin.php">Magasin</a>
            <img src="./images/site/icones/magasin.png" />
        </li>
        <li class="page-link">
            <a>Me contacter</a>
            <img src="./images/site/icones/me_contacter.png" />
        </li>
        <li class="page-link">
            <a>Blog</a>
            <img src="./images/site/icones/blog.png" />
        </li>
	</ul>
</aside>


<nav id="top-outils-bar">    
    <div id="shoppingcard-link">
        <img src="./images/site/icones/panier3.png" />
        <a>Panier</a>
            
        <div id="shoppingcard-box-wrap">
            <div id="shoppingcard-box"></div>
        </div>
    </div>
        
    
    <div id="useraccount-link">
        <img src="./images/site/icones/utilisateur.png" />    
        
        <?php           
            
        if (isset($_SESSION["client"])) {
              
            echo "<a>";
            echo $_SESSION['client']['pseudo'];
            echo "</a>";
                
            //echo "<div id='disconnect-box'></div>";
        }
        else {
            echo "<a>Connexion</a>";
                
        }
            
        ?>        
         
    </div>
        
        
    <div id="disconnect-box-wrap">
            <div id="disconnect-box">
                <ul>
                    <li class="disconnect-button">Deconnexion</li>
                    <li class="outils-button">Options</li>
                </ul>
                
            </div>
        </div>
        

</nav>


<div id="top-bar-corner">
    <img src="./images/site/icones/recherche.png" />    
</div>


<!-- CONNEXION -->
<div id="overlay-background"></div>    
<div id="login-box">    
    <p class='close-box'>x</p>
        
    <form id="login-form">
            
        <fieldset>
        <legend>Se connecter</legend>
		    
        <input type="text" id="pseudo" name="pseudo" placeholder="Pseudo">
		<br />
			
		<input type="password" id="mdp" name="mdp" placeholder="Mot de passe">
        <br />        
 
        <button type="button" name="connexion" class="login-button">Se connecter</button>
            
        <p class="login-error-msg"></p>
            
    	</fieldset>
	</form>	
        
    <p class="redirect-msg">S'inscrire</p>        
</div>
	
<!-- INSCRIPTION -->
<div id="signup-box">    
    <p class='close-box'>x</p>
        
    <form id="signup-form">
            
        <fieldset>
        <legend>S'inscrire</legend>
		    
        <input type="text" id="pseudo" name="pseudo" placeholder="Pseudo">
		<br />
			
		<input type="password" id="mdp" name="mdp" placeholder="Mot de passe">
        <br />
            
        <input type="adresse" id="adresse" name="adresse" placeholder="Adresse">
        <br />
            
        <input type="telephone" id="telephone" name="telephone" placeholder="Telephone">
        <br />
 
        <button type="button" name="connexion" class="signup-button">S'inscrire</button>
            
        <p class="signup-error-msg"></p>
            
    	</fieldset>
	</form>	
        
    <p class="redirect-msg">Se connecter</p>        
</div>
	
		
   

