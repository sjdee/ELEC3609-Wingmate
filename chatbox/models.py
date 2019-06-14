from django.db import models
from django.contrib.auth.models import User
from django_bleach.models import BleachField


#Model for the chatroom relationship between two users
class Chatroom(models.Model):
	#userOne and userTwo are representations of a sender and a receiver
	userOne = models.ForeignKey(User, related_name='%(class)s_userOne', null=True)
	userTwo = models.ForeignKey(User, related_name='%(class)s_userTwo', null=True)

	def __str__(self):
		return str(self.userOne.username) + " and " + self.userTwo.username

	class Meta:
		unique_together = ('userOne', 'userTwo')

#Model for the message data between two users
class Message(models.Model):
	#Limit content space to 500 to prevent nefariously sized messages
	content = models.CharField('content', max_length=500)
	content = BleachField()
	sender = models.ForeignKey(User, null=True)
	chatroom = models.ForeignKey(Chatroom, default=None)

	def __str__(self):
		return "#" + str(self.pk) + " to '"+  str(self.chatroom) + "' chatroom"
