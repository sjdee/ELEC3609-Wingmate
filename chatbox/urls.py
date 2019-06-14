from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^chatbox/$', views.chatbox_index, name='chatbox'),
	url(r'^chatbox/(?P<chatroom_id>[0-9]+)/$', views.chatbox, name="chatroom"),
	url(r'^ajax/post-message/$', views.post_message, name='post_message'),
	url(r'^ajax/load-all-messages/$', views.load_all_messages, name='load_all_messages'),
	url(r'^ajax/all_chatroom/$', views.all_chatrooms, name='all_chatrooms'),
	url(r'^ajax/user_chatroom/$', views.user_chatroom, name='user_chatrooms')


]
