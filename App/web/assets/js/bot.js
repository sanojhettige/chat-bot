    /*================================
    Scroll to last message
    ==================================*/
    function scrollbottom(){
        var height = 0;
        height = $('.direct-chat-messages').height();
        $('.direct-chat-messages').animate({scrollTop: 20000000 });
    }

    /*================================
    Send user request
    ==================================*/
    function send_messenger(){
        var text_messenger = $('#text_messenger').val();
        doGetBotResponse(text_messenger, false);
    }

    /*================================
    Get BOT response
    ==================================*/
    function doGetBotResponse(message, firstMessage) {
        if(message){
            if(!firstMessage) {
                $('.direct-chat-messages').append('<div class="chat_msg_item chat_msg_item_user">\
                    <img class="chat_avatar" src="assets/images/avatar.png" alt="Image">\
                    <div class="direct-chat-text">\
                    '+ message +'\
                    </div>\
                    </div>');
            }
            $.post("http://127.0.0.1:4000/getresponse", {query: message}, function(result){
                res = JSON.parse(result);

                if(res['status'] == 'success'){

                    if(res['content']['ti_le'] >= 0.3){
                        response_bot = res['content']['answer'];
                    }else{
                        response_bot = 'Did you mean "'+ res['content']['question'] +'" <br>';
                        response_bot += res['content']['answer'];
                    }
                }else{
                    response_bot = "Sorry, the bot doesn't get what you said";
                }
                $('.direct-chat-messages').append('<div class="chat_msg_item chat_msg_item_admin">\
                    <img class="chat_avatar" src="assets/images/bot.png" alt="Image">\
                    <div class="direct-chat-text">\
                    '+ response_bot +'\
                    </div>\
                    </div>');
                $('#text_messenger').val('');
            });
            scrollbottom();
        }
    }

    /*================================
    Send Message
    ==================================*/
    $('#send_messenger').click(function(){
        send_messenger();
    });

    /*================================
    Send message on enter
    ==================================*/

    $('#text_messenger').keypress(function(e) {
        if(e.which == 13) {
            send_messenger();
        }
    });

    /*================================
    Get first reponse from BOT
    ==================================*/
    doGetBotResponse('hello', true);
