<p>

$(".content").mCustomScrollbar({
    horizontalScroll:true
});

jquery.mCustomScrollbar.css contains few ready-to-use scrollbar themes that you can apply easily on your scrollbars by setting the theme option parameter to the theme name you want

No wrapjavascript

$(".content").mCustomScrollbar({
    theme:"light"
});

Additional demos & examples▾
Detailed usage guide
</p>


<p>
jquery.mCustomScrollbar.css contains the basic styling of the custom scrollbar and should normally be included in the head tag of your html (typically before any script tags). If you wish to reduce http requests and/or have all your website stylesheet in a single file, you should move scrollbars styling in your main CSS document.

mCSB_buttons.png is a single PNG image file that contains the default, plus some additional sets for the up, down, left and right arrows used by the scrollbar buttons. I’ve created a single file in order to use CSS sprites for the button icons (defined in jquery.mCustomScrollbar.css). The plugin archive contains the PSD source (source_files/mCSB_buttons.psd) so you can add your own if you wish.

jquery.mCustomScrollbar.concat.min.js is the main plugin file which contains the custom scrollbar script as well as all necessary scripts, plugins etc. concatenated and minified. This file should be included after loading the jQuery library (the javascript library used by the plugin).

Both jQuery and plugin files can be included inside the head or body tags of your document. Including scripts at the bottom of html documents (e.g. just before the closing body tag) is usually recommended for better performance. You can load jQuery via Google’s CDN (why?) or from your own directory (the archive contains a copy of jQuery inside js folder).

The way I recommend and what I’ve used in all demos and examples is loading jQuery from a CDN (e.g. Google) and have a local copy to fallback in case CDN files won’t load

No wraphtml

Call mCustomScrollbar function after jQuery and jquery.mCustomScrollbar.concat.min.js script tags. The HTML should look something like this:

No wraphtml
</p>

Detailed usage guide

<p>

jquery.mCustomScrollbar.css contains the basic styling of the custom scrollbar and should normally be included in the head tag of your html (typically before any script tags). If you wish to reduce http requests and/or have all your website stylesheet in a single file, you should move scrollbars styling in your main CSS document.

mCSB_buttons.png is a single PNG image file that contains the default, plus some additional sets for the up, down, left and right arrows used by the scrollbar buttons. I’ve created a single file in order to use CSS sprites for the button icons (defined in jquery.mCustomScrollbar.css). The plugin archive contains the PSD source (source_files/mCSB_buttons.psd) so you can add your own if you wish.

jquery.mCustomScrollbar.concat.min.js is the main plugin file which contains the custom scrollbar script as well as all necessary scripts, plugins etc. concatenated and minified. This file should be included after loading the jQuery library (the javascript library used by the plugin).

Both jQuery and plugin files can be included inside the head or body tags of your document. Including scripts at the bottom of html documents (e.g. just before the closing body tag) is usually recommended for better performance. You can load jQuery via Google’s CDN (why?) or from your own directory (the archive contains a copy of jQuery inside js folder).

The way I recommend and what I’ve used in all demos and examples is loading jQuery from a CDN (e.g. Google) and have a local copy to fallback in case CDN files won’t load 
The code is wrapped in (function($){ ... })(jQuery);. This ensures no conflict between jQuery and other libraries using $ shortcut (see Using jQuery with Other Libraries for more info). The plugin function is called on window load ($(window).load()) so it executes after all page elements are fully loaded, ensuring the script calculates correctly content’s length.
If the scrollbars apply to content that has no elements with external sources (e.g. images, objects etc.) you may want to call mCustomScrollbar on document ready (so code executes when the DOM is ready) 

</p>

<p>

jquery.mCustomScrollbar.css contains the basic styling of the custom scrollbar and should normally be included in the head tag of your html (typically before any script tags). If you wish to reduce http requests and/or have all your website stylesheet in a single file, you should move scrollbars styling in your main CSS document.

mCSB_buttons.png is a single PNG image file that contains the default, plus some additional sets for the up, down, left and right arrows used by the scrollbar buttons. I’ve created a single file in order to use CSS sprites for the button icons (defined in jquery.mCustomScrollbar.css). The plugin archive contains the PSD source (source_files/mCSB_buttons.psd) so you can add your own if you wish.

jquery.mCustomScrollbar.concat.min.js is the main plugin file which contains the custom scrollbar script as well as all necessary scripts, plugins etc. concatenated and minified. This file should be included after loading the jQuery library (the javascript library used by the plugin).

Both jQuery and plugin files can be included inside the head or body tags of your document. Including scripts at the bottom of html documents (e.g. just before the closing body tag) is usually recommended for better performance. You can load jQuery via Google’s CDN (why?) or from your own directory (the archive contains a copy of jQuery inside js folder).

The way I recommend and what I’ve used in all demos and examples is loading jQuery from a CDN (e.g. Google) and have a local copy to fallback in case CDN files won’t load 
The code is wrapped in (function($){ ... })(jQuery);. This ensures no conflict between jQuery and other libraries using $ shortcut (see Using jQuery with Other Libraries for more info). The plugin function is called on window load ($(window).load()) so it executes after all page elements are fully loaded, ensuring the script calculates correctly content’s length.
If the scrollbars apply to content that has no elements with external sources (e.g. images, objects etc.) you may want to call mCustomScrollbar on document ready (so code executes when the DOM is ready) 

</p>