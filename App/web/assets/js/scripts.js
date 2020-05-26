
(function($) {
    "use strict";

    /*================================
    Preloader
    ==================================*/

    var preloader = $('#preloader');
    $(window).on('load', function() {
        preloader.fadeOut('slow', function() { $(this).remove(); });
    });


    hideChat(0);

	$('.bot_opener').click(function() {
	  toggleFab();
	});


	//Toggle chat and links
	function toggleFab() {
	  $('.prime').toggleClass('zmdi-comment-outline');
	  $('.prime').toggleClass('zmdi-close');
	  $('.prime').toggleClass('is-active');
	  $('.prime').toggleClass('is-visible');
	  $('.chat').toggleClass('is-visible');
	  $('.fab').toggleClass('is-visible');
	  
	}


	function hideChat(hide) {
	    $('#chat_converse').css('display', 'block');
	}

})(jQuery);


