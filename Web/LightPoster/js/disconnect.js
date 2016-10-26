// LOGIN.JS
// Ensemble de fonctions permettant de se connecter/enregistrer sur le site

// -----------------------------------------------------------------------
//  @ MAIN
//  ----------------------------------------------------------------------
$(function () {
	disconnectPanel = $("#disconnect-box");
	userAccountLink = $("#useraccount-link");
	
	disconnectButton = $("#disconnect-box .disconnect-button");
	
	disconnectButton.click (function () {
		disconnect();
		disconnectPanel.fadeOut(300);
	});
	
	$("#useraccount-link, #shoppingcard-link").click(function () {
        openPopup(loginBox, overlay, 500);
    });
	
    userAccountLink.hover(
		function () {
			disconnectPanel.fadeIn(300);
		},
		function () {
			disconnectPanel.fadeOut(300);
		});
		
	disconnectPanel.hover(
		function () {
			disconnectPanel.stop(true).fadeIn();
		},
		function () {
			disconnectPanel.fadeOut(300);
		}
	);
});


// -----------------------------------------------------------------------
//  @ FONCTIONS
//  ----------------------------------------------------------------------
// Centre la fênetre de login ou inscription à l'écran
function centerWindow(window) {
    window.css({
        'position': 'fixed',
        'left': '50%',
        'top': '50%',
        'margin-left': -window.width() / 2,
        'margin-top': -window.height() / 2
    });
}

// Fait apparâitre la fênetre et eventuellement un overlay
function openPopup(window, overlay, fadeTime) {
    window.fadeIn(fadeTime);
    overlay.fadeIn(fadeTime);
}

// Fait disparâitre la fênetre et l'overlay
function closePopup(window, overlay, fadeTime) {
    window.fadeOut(fadeTime);
    overlay.fadeOut(fadeTime);
}

// Function permettant de se connecter au site
function login(loginBox, errorMsg) {
    $.post("./connexion.php", {        
        pseudo: $("#login-form #pseudo").val(), 
        mdp: $("#login-form #mdp").val()
    },     

    function (msg) {
        if (msg == 1) {
            errorMsg.hide();
            errorMsg.html("L'utilisateur n'existe pas.");
            errorMsg.fadeIn(300);
        }
        else if (msg == 2) {
            errorMsg.hide();
            errorMsg.html("Mot de passe incorrect.");
            errorMsg.fadeIn(300);
        }
        else if (msg == 3) {
            errorMsg.hide();
            errorMsg.html("Vous êtes à présent connecté au site !");
            errorMsg.css("color", "green");
            errorMsg.fadeIn(300);

            setTimeout(function () {
                window.location.href = "./index.php";
            }, 2000);
        }
    });
}

function disconnect() {
	$.get("./deconnexion.php");
	setTimeout(function ()	{
		window.location.href = "./index.php";
    }, 1500);	 
}
