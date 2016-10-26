// -----------------------------------------------------------------------
//  @ MAIN
//  ----------------------------------------------------------------------

$(function (pagebody) {
    mainWindow = $(window);
    
    // Paramètres pour définir la taille de la page
    var pagebody = new Object();
    pagebody.window = $("#pagebody");
    pagebody.marginTop = 180;
    pagebody.marginRight = 250;
    pagebody.marginBottom = 130;
    pagebody.marginLeft = 480;

    setPagebodySize(pagebody);
    
    mainWindow.resize(function () {
        setPagebodySize(pagebody);        
    });
});


function setPagebodySize(pagebody) {
    height = mainWindow.height() - (pagebody.marginTop + pagebody.marginBottom);
    width = mainWindow.width() - (pagebody.marginRight + pagebody.marginLeft);

    pagebody.window.css("width", width);
    pagebody.window.css("height", height);
    pagebody.window.css("margin-left", pagebody.marginLeft);
    pagebody.window.css("margin-top", pagebody.marginTop);    
}