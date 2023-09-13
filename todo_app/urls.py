from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserCreate

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('users/', UserCreate.as_view(), name='create-user'),

]
