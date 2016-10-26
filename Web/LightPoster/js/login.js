// LOGIN.JS
// Ensemble de fonctions permettant de se connecter/enregistrer sur le site

// -----------------------------------------------------------------------
//  @ MAIN
//  ----------------------------------------------------------------------
$(function () {
    // ---------------- LOGIN BOX ----------------
    loginBox = $("#login-box");
    overlay = $("#overlay-background");

    loginErrorMsg = $(".login-error-msg");
    signupErrorMsg = $(".signup-error-msg");

    centerWindow(loginBox);      

    $("#useraccount-link, #shoppingcard-link").click(function () {
        openPopup(loginBox, overlay, 500);
    });

    $("body").on('click', "#overlay-background", function () {
        closePopup(loginBox, overlay, 500);
        closePopup(signupBox, overlay, 500);
        loginErrorMsg.fadeOut(500);
    });

    $("#login-box").on('click', ".close-box", function () {
        closePopup(loginBox, overlay, 500);
        loginErrorMsg.fadeOut(500)
    });

    // Lorsqu'on appuye sur le bouton pour se connecter ...
    $("#login-form").on('click', ".login-button", function () {    
        loginErrorMsg.hide();
        login(loginBox, loginErrorMsg);
        loginErrorMsg.fadeIn(300);
    });
    
    $("#login-box").on("click", ".redirect-msg", function () {
        switchWindows(signupBox, loginBox);
        loginErrorMsg.hide();
    });

    // ---------------- SIGN UP BOX ----------------
    signupBox = $("#signup-box");
    
    centerWindow(signupBox);
    
    $("#signup-box").on("click", ".redirect-msg", function () {
        switchWindows(loginBox, signupBox);
        signupErrorMsg.hide();
    });

    $("#signup-box").on('click', ".close-box", function () {
        closePopup(signupBox, overlay, 500);
        signErrorMsg.fadeOut(500)
    });

    $("#signup-form").on('click', ".signup-button", function () {
        signupErrorMsg.hide();
        signup(signupBox, signupErrorMsg);
        signupErrorMsg.fadeIn(300);
    });
});


// -----------------------------------------------------------------------
//  @ FONCTIONS
//  ----------------------------------------------------------------------
// Function permettant de s'enregistrer sur le site
function signup(signUpBox, errorMsg) {
    $.post("./inscription.php", {
        pseudo: $("#signup-form #pseudo").val(),
        mdp: $("#signup-form #mdp").val(),
        adresse: $("#signup-form #adresse").val(),
        telephone: $("#signup-form #telephone").val()
    },

    function (msg) {
         if (msg == 1) {
            errorMsg.css("color", "red");
            errorMsg.html("Le pseudo que vous avez entré existe déjà.");
        }
        else if (msg == 2) {
            errorMsg.css("color", "green");
            errorMsg.html("Vous avez été enregistré avec succès !");

            setTimeout(function () {
                window.location.href = "./index.php";
            }, 1500);
        }
    });
}

// Function permettant de se connecter au site
function login(loginBox, errorMsg) {
    $.post("./connexion.php", {        
        pseudo: $("#login-form #pseudo").val(), 
        mdp: $("#login-form #mdp").val()
    },     

    function (msg) {
		
        if (msg == "Inexistant") {
            errorMsg.css("color", "red");
            errorMsg.html("L'utilisateur n'existe pas.");
        }
        else if (msg == "Mdp Incorrect") {
            errorMsg.css("color", "red");
            errorMsg.html("Mot de passe incorrect.");
        }
        else if (msg == "Connecté") {
            errorMsg.css("color", "green");
            errorMsg.html("Vous êtes à présent connecté au site !");

            setTimeout(function () {
                window.location.href = "./index.php";
            }, 1500);
        }
    }, "json");
}
