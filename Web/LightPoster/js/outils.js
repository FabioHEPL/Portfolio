// -----------------------------------------------------------------------
//  @ FONCTIONS
//  ----------------------------------------------------------------------
// Centre la fênetre de login ou inscription à l'écran
function centerWindow(window) {
    console.log("centering ...");

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

function switchWindows(winA, winB) {
    winA.fadeIn(300);
    winB.fadeOut(100);
}


// -----------------------------------------------------------------------
//  @ PARAMÈTRES DE LA SCROLLBAR
//  ----------------------------------------------------------------------
$(function () {
    $("#pagebody").mCustomScrollbar({            
        autoHideScrollbar: true,
	    scrollInertia: 0,
	    autoDraggerLength: true,
	    mouseWheel: true,

        advanced:{
            updateOnBrowserResize: true,
            updateOnContentResize: true
        }            
    });
});
