from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks']

    
class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'created_at', 'status', 'assignee', 'completed_at']
        read_only_fields = ['id', 'created_at', 'completed_at'] 

    def create(self, validated_data):
        assignees = validated_data.pop('assignee', [])
        task = Task.objects.create(**validated_data)

        if validated_data.get('status') == 'completed':
            task.completed_at = timezone.now()

        if assignees:
            task.assignee.set(assignees) 

        return task