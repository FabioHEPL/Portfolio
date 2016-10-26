<?php session_start(); ?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Light Poster • Accueil</title>
    <link href="jquery.mCustomScrollbar.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" href="styles/style.css">
    
</head>

<body>

<?php 

include("uimenu.php");

?>

<div id="pagebody">
	<div id="section-title">
		<p>Accueil</p>
	</div>
	
    <h1 class="welcome-title">Bienvenue sur LightPoster !</h1>
    
        
</div>

<script src="js/jquery.js"></script>
<script src="js/window_fix.js"></script>
<script src="js/center.js"></script>
<script src="js/outils.js"></script>
<script src="js/scrollbar.js"></script>
<script src="jquery.mCustomScrollbar.concat.min.js"></script>
<script>
    (function($){
        $(window).load(function(){
            $("#pagebody").mCustomScrollbar({
            
            autoHideScrollbar: true,
			scrollInertia: 0,
   
            advanced:{
                updateOnBrowserResize: true
            }
            
            
            });
        });
    })(jQuery);
</script>

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
