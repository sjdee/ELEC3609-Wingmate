#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
#replace the app_id, key and secret are from the account I made in Pusher website.
from .models import Message, Chatroom

from django.core import serializers

#decorators for use in views
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token


# the following two libraries are used for the server side of the chatbox.
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt # for the sake of testing, ignore the csrf tokens.

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Q #used for advanced queries

#Third-party packages
from pusher import Pusher #used for client to client messaging service
from django_bleach.models import BleachField



#instantate the pusher class
pusher = Pusher(app_id=u'418592', key=u'5ee5f4fda82c77f41ed5', secret=u'6b2b6e996c3080e170d9')


#this view is to redirect to the chatbox - earliest one
def chatbox_index(request):
    current_user = request.user
    chatroom = Chatroom.objects.filter(Q(userOne=current_user) | Q(userTwo=current_user)).first()
    all_chatrooms = Chatroom.objects.filter(Q(userOne =current_user) | Q(userTwo=current_user))
    if chatroom == None:
         return render(request, 'chatbox/chatbox-none.html', context=None)
    return render(request,'chatbox/chatbox.html', context={'chatroom' : chatroom, 'all_chatrooms' : all_chatrooms});


#
#login required to access this page. will redirect to admin login page.
#View serves an AJAX page
#the view returns the chatroom for the chatroom display, for a given chatroom id
@login_required(login_url='/admin/login/')
def chatbox(request, chatroom_id):
    current_user = request.user

    #ensures that the chatroom exists
    try:
        chatroom = Chatroom.objects.get(id=chatroom_id) #need to create
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    #ensures that the user belongs to the chatroom
    if (current_user.id != chatroom.userOne_id and current_user.id != chatroom.userTwo_id):
        return HttpResponseNotFound('<h1>Page not found</h1>')

    all_chatrooms = Chatroom.objects.filter(Q(userOne=current_user) | Q(userTwo=current_user)) #all of a user's chatrooms
    context = {'chatroom' : chatroom, 'all_chatrooms' : all_chatrooms} #chatroom stores the current chatroom, all_chatrooms for the side display
    return render(request,'chatbox/chatbox.html', context=context);


@requires_csrf_token
@login_required(login_url='/login/')
def post_message(request):
    if request.method == 'POST':
        x = request.POST.get("chatroom_id")
        print(x)
        chatroom = Chatroom.objects.get(pk=x) #need to GET this from request
        pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
        content = request.POST.get('message')
        sender = User.objects.get(username=request.user.username) #get the sender object
        newMessage = Message(content=content, sender=sender,chatroom=chatroom) #create a new message for chat room
        newMessage.save()
        return HttpResponse("done");


@requires_csrf_token
@login_required(login_url='/login/')
def load_all_messages(request):
    if request.method == 'POST':
        x = request.POST.get("chatroom_id")
        print(x)
        chatroom = Chatroom.objects.get(pk=x) #need to GET this from request
        messages = Message.objects.filter(chatroom=chatroom).values('content', 'sender_id')
        participants = {}
        new_messages = []
        for message in messages:
            sender_id = message['sender_id']
            if message['sender_id'] in participants:
                username = participants[str(sender_id)]
            else:
                if (message['sender_id'] == None):
                    continue
                username = get_username_from_pk(int(message['sender_id']))
                participants.update({str(sender_id) : username} )
            content = message['content']
            new = dict({'content' : content, 'username' : username})
            new_messages.append(new)
        return JsonResponse({'results' : list(new_messages)})


def validate_chatroom(request):
    current_user = request.user




#AJAX function that serves all chats for a specific user#
@requires_csrf_token
@login_required(login_url='/login/')
def all_chatrooms(request):
    print("chatrooms request")
    current_user = request.user
    chats = []
    chatrooms = Chatroom.objects.filter(Q(userOne_id=current_user.id) | Q(userTwo_id=current_user.id)).values()
    for chat in chatrooms:
        print chat
        if request.user.id == chat['userOne_id']:
            other_user = User.objects.get(pk=int(chat['userTwo_id']))
        else:
            other_user = User.objects.get(pk=int(chat['userOne_id']))
        chats.append({'id' : chat['id'], 'other_user' : other_user.username })

    all_chat = {'chats' : chats}
    return JsonResponse(all_chat)


#AJAX function that serves for a specific chat room
#creates a chatroom between two users if one doesnt exist
    #needs the other user, uses the self refrences
@requires_csrf_token
@login_required(login_url='/login/')
def user_chatroom(request):
    current_user = request.user
    other_user = User.objects.get(username=request.POST.get('other_user'))
    #checks if there is already a chat room with the user, where the other user is 'userOne'
    try:
        chatroom = Chatroom.objects.get(userOne=current_user, userTwo=other_user)
    except ObjectDoesNotExist:
        try: #checks if there is already a chat room with the user, where the other user is 'userTwo'
            chatroom = Chatroom.objects.get(userOne=other_user, userTwo=current_user)
        except ObjectDoesNotExist:  #otherwise create a new chatroom
            chatroom = Chatroom.objects.create(userOne=current_user, userTwo=other_user)

    return JsonResponse({'chatroom_id' : chatroom.id}) #returns the id of the chatroom
    # return HttpResponse('<a href=/chatbox{0}></a>'.format(chatroom.id))


def get_username_from_pk(sender_id):
    username = User.objects.get(pk=sender_id).username
    return username
