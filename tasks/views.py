from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def assign_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    user_ids = request.data.get('assignee', [])
    users = User.objects.filter(id__in=user_ids)

    if not users:
        return Response({'error': 'No valid users found'}, status=status.HTTP_400_BAD_REQUEST)
    
    task.assignee.add(*users)
    task.save()

    return Response(data={"message": "user assigned successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_tasks(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(user.tasks.all(), many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)