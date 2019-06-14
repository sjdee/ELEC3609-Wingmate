//Builds the marker's popup on insitalisation
    //also adds listenrs for any potential interactions
function buildPopup(feature, layer, data) {
    var container = $('<div />');// Delegate all event handling for the container itself and its contents to the container

    //listener to trigger star ratings
    container.on('click', '.star-button', function(data) {
        var cont = container[0]
        var rating_data = data.target.value

        var csrftoken = getCookie('csrftoken');
        //post request to the server of the given rating
        $.post({
           type:"POST",
           url: 'ajax/user_review/',
           data: {
           'username' : feature.properties.name,
           'rating' : rating_data,
           'csrfmiddlewaretoken': csrftoken,
           },
           success: function (data) {
               container.html(popupContent + end)
               setRatingInput(cont, rating_data) // sets the rating in the front end
               $('#info-display').html("you rated " + feature.properties.name+ " : ")

               setTimeout(function() {
                   //need to update the current rating
                   var name = feature.properties.name;
                   var namerefrence = feature.properties.name + "'s";
                  $('#info-display').html(namerefrence + " average rating:")
                  resetAverageStarRating(cont, feature.properties.name)

              }, 2000)

           }
        });

    });

    //listener for the messsage button, triggered when an element on the popup is clicked
    container.on('click',  '#message-button', function(e) {
        var csrftoken = getCookie('csrftoken');
        data = {'other_user' : feature.properties.name, 'csrfmiddlewaretoken': csrftoken,} //name tied to the popup
        //other_user is the name of the clicked popup
          $.post({
              type:"POST",
              url: 'ajax/user_chatroom/',
              data: data,
              success: function (e) {
                  window.location.href = "/chatbox/" + e.chatroom_id
              }
        });
    })

    container.on('click',  '#profile-button', function(e) {
         window.location.href = "/profile/"
    })

    var name = feature.properties.name;
    var namerefrence = feature.properties.name + "'s";
    if (data.isCurrent)  { name = 'You'; namerefrence = 'Your'}

    var popupContent =
    `<div class="content">
        <img src="/static/images/default.jpg" width=256 height=256 style="border-radius:50%"> </img>
        <h1>`+ name +`</h1>
        <p id="info-display">` + namerefrence + ` average rating: </p>
    <div>
    <fieldset class="rating">
        <input class="star-button" type="radio" id="star4" name="rating" value="4" /><label class = "full actual-rating" for="star4" title="Best it can be - 4 stars"></label>
        <input class="star-button" type="radio" id="star3" name="rating" value="3" /><label class = "full" for="star3" title="Meh - 3 stars"></label>
        <input class="star-button" type="radio" id="star2" name="rating" value="2" /><label class = "full" for="star2" title="Not great ay - 2 stars"></label>
        <input class="star-button" type="radio" id="star1" name="rating" value="1" /><label class = "full" for="star1" title="Quit - 1 stars"></label>
        </fieldset>
    </div>
    <div id='button-div'>
    `
    console.log(data.isCurrent)
    if (data.isCurrent) {
        var end = `<button class="button" id="profile-button">view profile</button></div>`
    }
    else if (data.canAccess) {
        var end = `<button class="button" id="message-button">send message</button></div>
        </div>`
    }
    else {
        var end = `<button class="button" disabled='true' id="message-button-disabled">get premium to send message</button></div></div>`
    }


    container.html(popupContent + end)
    layer.bindPopup(container[0])
}
