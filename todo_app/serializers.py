from rest_framework import serializers
from rest_framework.authtoken.models import Token

from datetime import date
from django.contrib.auth.models import User

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
    

class UserSerializer(serializers.ModelSerializer):
    """Creating Serializers for the Users"""

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Overriding the default create User method to save User Instances"""
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
