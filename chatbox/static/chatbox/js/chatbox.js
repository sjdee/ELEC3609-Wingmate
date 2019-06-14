//initiate puhser with your application key
var pusher = new Pusher('5ee5f4fda82c77f41ed5');
//subscribe to the channel you want to listen to
var my_channel = pusher.subscribe('a_channel');
//wait for an event to be triggered in that channel



function load_messages() {

	var csrf = '{{ csrf_token }}';
	var csrftoken = getCookie('csrftoken');

	$.post({
		type:"POST",
		url: '/ajax/load-all-messages/',
		data: {
		'chatroom_id' : chatroom_id ,
		'csrfmiddlewaretoken' : csrftoken,
		},

		success: function (e) {
			messages = e.results
	        for (i = 0; i < messages.length; i++) {
	            message = messages[i]
	            push_message(message.username, message.content)
	        }

		}
	});
}

function push_message(name, message) {
    if (name == user) {
        var  new_message_user = `
        <li class="list-group-item right">
            <div id="message-body"> <label id="message-text">`
                + message +` </label>
                <img src= "{% static 'chatbox/img/default.jpg'%}"" >
            </div>
        </li>`
    }
    else {
        var  new_message_user = `
        <li class="list-group-item left">
            <div id="message-body">
                <img src= {% static 'chatbox/img/default.jpg'%} >
                <label id="message-text">
                `+ message +
            `</label>
        </div>
    </li>`
    }
 //append the new message to the ul holding the chat messages
$('#chat').append(new_message_user);
}

my_channel.bind("an_event", function (data) {
    push_message(data.name, data.message)
});

//wait until the DOM is fully ready
$(document).ready(function(){
    console.log($(window).height())
    console.log($(document).height())

	// enter key
        $(document).bind('keypress', function(e) {
            if(e.keyCode==13){
                 $('#btn-chat').trigger('click');
             }
        });

    setContentHeight('#chat')
    $('#chat').animate({scrollTop: $('#chat').prop("scrollHeight")}, 500);
    load_messages()
    //add event listener to the chat button click
    $("#btn-chat").click(function(){
        //get the currently typed message
         var message = sanitize($('#btn-input').val());
		 var csrftoken = getCookie('csrftoken');

        $.post({
			type:"POST",
            url: '/ajax/post-message/',
            data: {
            'message': message,
            'chatroom_id': chatroom_id,
			'csrfmiddlewaretoken': csrftoken,
            },
            success: function (data) {

                $('#btn-input').val('');

            }
        });

    })
})

function sanitize(input) {
	// console.log('chains and whips');
	var output = input.replace(/<script[^>]*?>.*?<\/script>/gi, '').
					 replace(/<[\/\!]*?[^<>]*?>/gi, '').
					 replace(/<style[^>]*?>.*?<\/style>/gi, '').
					 replace(/<![\s\S]*?--[ \t\n\r]*>/gi, '');

	    return output;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function setContentHeight(element, offset) {
    $(element).css("height", $(window).height() - 250)
    $(window).resize(function() {
        $(element).css("height", $(window).height() - 250)
    });
}
