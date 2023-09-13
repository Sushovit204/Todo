from rest_framework import serializers
from datetime import date

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Creating serializers for the Task Model"""

    class Meta:
        """Specifying the model and fields on which the serializer is working"""
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        """Check if the due date is already gone"""
        if value < date.today():
            raise serializers.ValidationError("Due date must be in future")
        return value