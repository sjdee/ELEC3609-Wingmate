
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, WingmanLocationSerializer, ChatroomSerializer

from wingmap.models import WingmanLocation
from chatbox.models import Chatroom
from django.contrib.auth.models import User, Group



class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class WingmanLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WingmanLocation.objects.all()
    serializer_class = WingmanLocationSerializer


class ChatroomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to retrieve all their chats
    """
    queryset = Chatroom.objects.all()
    serializer_class = ChatroomSerializer
