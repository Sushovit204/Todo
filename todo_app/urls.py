from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserCreate, LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('users/', UserCreate.as_view(), name='create-user'),

]
