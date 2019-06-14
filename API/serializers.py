from rest_framework import serializers

from django.contrib.auth.models import User, Group
from wingmap.models import WingmanLocation
from chatbox.models import Chatroom


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class WingmanLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WingmanLocation
        geo_field = "geom"
        fields = ('name', 'geom')


class ChatroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chatroom
        fields = ('userOne', 'userTwo')
