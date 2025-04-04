from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from messaging.socketio_server import socketio

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        socketio.emit('new_message', {
            'id': message.id,
            'sender': message.sender,
            'content': message.content,
            'timestamp': message.timestamp.isoformat()
        })










        