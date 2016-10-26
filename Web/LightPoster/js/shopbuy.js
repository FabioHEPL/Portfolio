// SHOPBUY.JS
// Ensemble de fonctions permettant d'acheter un ou plusieurs articles sur le site
// -----------------------------------------------------------------------
//  @ MAIN
//  ----------------------------------------------------------------------
$(function () {
    // ---------------- ACHAT MAGASIN ----------------    
    alertBox = $("#alert-box");

    centerWindow(alertBox);

    alertBox.on('click', ".a-close-box", function () {
        closePopup(alertBox, $("#overlay-background"), 500);
    });

    $("body").on('click', "#overlay-background", function () {
        closePopup(alertBox, $("#overlay-background"), 500);
    });

    $("#product-form button.buyproduct-button").on('click', '', function () {
		var product = $(this).closest("form");
		
		quantity = product.find(".quantity-field").val();
		productCode = product.find("input[name='code_article']").val();
		
		buyProduct(productCode, quantity);
		
    });   
});


function buyProduct(productCode, quantity) {
    $.post("./update_panier.php", {
        action: "achat",
        code_article: productCode, 
        quantite: quantity
    },     

    function (data) {
        if (data.message == "NotConnected") {
            openPopup($("#login-box"), $("#overlay-background"), 500);
        }
        else if (data.message == "SuccessfulPurchase") {
            alertBox = $("#alert-box");
            openPopup(alertBox, $("#overlay-background"), 500);
            alertBox.find("h1").html("<h1 class='error-alert'>L'article a été ajouté au panier</h1>");
        }
        else if (data.message == "QuantityExceed") {
            alertBox = $("#alert-box");
            openPopup(alertBox, $("#overlay-background"), 500);
            msg = "<h1 class='error-alert'>La quantité que vous avez choisie dépasse la quantité en stock." +
                  "<br />Quantité choisie (en total) : " + data.chosenQuantity + "  | Quantité restante : " + data.availableQuantity + "</h1>";

            alertBox.find("h1").html(msg);
        }
    }, "json");
}


