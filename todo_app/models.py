from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Model for tasks"""
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """String representation of the Task model"""
        return self.question