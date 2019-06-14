//helper function that checks the input buttons of the star
function setRatingInput(container, rating) {
    var button = container.getElementsByClassName('star-button')[4 - rating]
    button.checked = true;
}

function resetAverageStarRating(container, username) {
    var csrftoken = getCookie('csrftoken');
    $.get({
        type:"GET",
        url: 'ajax/user_review/',
        data: {
            'username' : username,
            'csrfmiddlewaretoken': csrftoken,
        },
        success: function (data) {
            rating = data['rating']
            if (rating == 0){
                return;
            }
            setRatingInput(container, rating)
        }
    });
}


//zooms to the current user on the map, with an offset
function zoom(latlng) {
    var point = $.map.latLngToLayerPoint(latlng)
    var offset = $.map.getSize().y*0.2
    var new_lng = point.y - offset
    var new_point = new L.Point(point.x, new_lng)
    var new_marker = $.map.layerPointToLatLng(new_point)

    $.map.panTo(new_marker, {animate: true});
}


function clickZoom(e) {
    zoom(e.latlng)
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

function setContentHeight(element) {
    $(element).css("height", $(window).height())
    $(window).resize(function() {
        $(element).css("height", $(window).height())
    });
}
