from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer, UserSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """View for getting List of Tasks and Post a Task"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for Get, Update, Delete Task by pk"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserCreate(generics.CreateAPIView):
    """View for creating User"""
    authentication_classes = () #Giving exemption to UserCreate for authentication and permission by overiding global settings
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    """View for the user to get token when they have permission"""
    permission_classes = ()

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username = username, password = password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, 
                            status= status.HTTP_400_BAD_REQUEST)