function onEachFeature(feature, layer) {
    var csrftoken = getCookie('csrftoken');

  $.get({
      type:"GET",
      url: 'ajax/user_review/',
      data: {
      'username' : feature.properties.name,
      'csrfmiddlewaretoken': csrftoken,
      },
      success: function (data) {
         buildPopup(feature, layer, data)
      }
});
}

//updates the map wihth the user locations from server
// function updateMarkers(map) {
//     var icon = L.icon({
//         iconUrl: "{% static 'images/iconw.png' %}",
//         shadowUrl : "{% static 'images/iconwshadow.png' %}",
//
//         shadowSize: [40,46],
//         iconSize:   [50, 46], // size of the icon
//         shadowAnchor: [35,0],
//         iconAnchor:   [40, 0], // point of the icon which will correspond to marker's location
//         popupAnchor:  [-10, 0] // point from which the popup should open relative to the iconAnchor
//     });
//
//     //retrieves all the locations from the server
//     $.getJSON("{% url 'wingmanLocation' %}", function (data) {
//         var names;
//         L.geoJson(data, {
//             pointToLayer: function(feature, latlng) {
//                 return L.marker(latlng, {icon:icon});
//             },
//             onEachFeature: onEachFeature,
//         }).addTo(map).on('click', clickZoom);
//     });
// }



//function that retrieves the current user's position
    //either through google geoocation api
    //or though the browser geoLocation - requires SSL though

function getLocation(isGoogle) {
    if (!isGoogle) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(post_location);
        }

    }
    else {
        $.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCmcIYxL2HuKsEPzKq2NQ8eOHoNEbkRoVk",
        function(position){
            post_location({coords : {'latitude' : position.location.lat, 'longitude' : position.location.lng}})
        })
    }
}

//makes ajax call to server
function post_location(position){
var data = {'lat' : position.coords.latitude,
'long': position.coords.longitude};
 $.map.setView([data.lat, data.long], 30)
$.ajax({
    type: "GET",
    url: '/ajax/user_location/',
    data: data,
    dataType: 'json',
    contentType:'application/json',
    success: function(data){
        console.log("this the data:", data);
    },
    complete: function() {
        updateMarkers($.map)
    }
});
}

//display's mates list on the side
function display_mateslist(all_mates) {
for (i = 0; i < all_mates.length; i++) {
    var list_element  =`<li class="list-group-item">
        <div class="wingmate-row" value=`+ all_mates[i].username +`>
            <img src="static/images/default.jpg" style="border-radius:50%; margin-right:15px">
            ` + all_mates[i].username +`
        </div>
    </li>`
    $('#mates-list').append(list_element);
}
}

function init_wingmatesMenu() {
    //sets up a listener for the clickable interface
    $('.wingmate-row').on('click', function(e) {
        name = e.target.getAttribute('value')
        $.map.eachLayer(function (layer) {
            if (layer.feature && name == layer.feature.properties.name) {
                $.map.closePopup()
                layer.openPopup()
                zoom(layer._latlng)
            }

    });
    })
}
