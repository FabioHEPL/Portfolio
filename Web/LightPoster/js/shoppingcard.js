// SHOPBUY.JS
// Ensemble de fonctions permettant de modifier/supprimer des articles dans le panier
// -----------------------------------------------------------------------
//  @ MAIN
//  ----------------------------------------------------------------------
$(function () {
    // ---------------- ACHAT MAGASIN ----------------    
    shoppingCard = $("#shopping-card");

    alertBox = $("#alert-box");

    centerWindow(alertBox);

    alertBox.on('click', ".a-close-box", function () {
        closePopup(alertBox, $("#overlay-background"), 500);
    });

    $("body").on('click', "#overlay-background", function () {
        closePopup(alertBox, $("#overlay-background"), 500);
    });

    $("#shopping-card button.deleteproduct").on('click', '', function () {
        var product = $(this).closest("tr");

        deleteProduct(product, shoppingCard);
    });

    $("#shopping-card button.modifyproduct").on('click', '', function () {
        var product = $(this).closest("tr");

        var productInfo = new Object();
        productInfo.productCode = product.find("input[name='code_article']").val();
        productInfo.quantity = product.find(".quantity-field").val();
        productInfo.subTotalField = product.find("td.product-td-subtotal");
        productInfo.price = product.find("td.product-td-price").text().split(" ")[0];
        productInfo.price = parseFloat(productInfo.price);
        productInfo.quantityTd = product.find("td.product-td-quantity");

        editProductQuantity(productInfo, shoppingCard);        

    });


});


// Enlève un article du panier
function deleteProduct(product, shoppingCard) {
    productCode = product.find("input[name='code_article']").val();


    $.post("./update_panier.php", {
        action: "remove",
        code_article: productCode
    },

    function (data) {
        if (data.message == "SuccessfulRemove") {            
            product.fadeOut(300, function () {
                $(this).remove();
                updateTotal(shoppingCard);
            });
        }
    },
    "json");
}


// Modifie la quantité d'un article
function editProductQuantity(productInfo, shoppingCard) {
    $.post("./update_panier.php", {
        action: "modifier",
        code_article: productInfo.productCode,
        quantite: productInfo.quantity
    },

    function (data) {
        
        if (data.message == "SuccessfulEdit") {
            subTotal = parseFloat(data.chosenQuantity) * productInfo.price;
            productInfo.subTotalField.html(subTotal + " €");
            productInfo.quantityTd.html(data.chosenQuantity);

            updateTotal(shoppingCard);
        }
        else if (data.message == "QuantityExceed") {
            alertBox = $("#alert-box");
            openPopup(alertBox, $("#overlay-background"), 500);
            msg = "<h1 class='error-alert'>La quantité que vous avez choisie dépasse la quantité en stock." +
            "<br />Quantité choisie : " + data.chosenQuantity + "  | Quantité restante : " + data.availableQuantity + "</h1>";

            alertBox.find("h1").html(msg);

            
        }


    }, "json");
}



function updateTotal(shoppingCard) {
    total = 0.0;

    shoppingCard.find("td.product-td-subtotal").each(function () {
        subTotal = $(this).text().split(" ")[0];

        total += parseFloat(subTotal);
    });   

    shoppingCard.find("td.product-td-total-num").html(total + " €");

    if (total <= 0) {
        shoppingCard.fadeOut(function () {
            $("#section-title").after("<p class='shoppingcardempty-message'>Votre panier est vide.</p>");
        });
    }
}