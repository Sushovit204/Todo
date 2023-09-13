from django.shortcuts import render
from rest_framework import generics

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
    serializer_class = UserSerializer