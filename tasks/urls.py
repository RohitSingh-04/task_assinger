from django.urls import path
from .views import create_user, create_task, assign_task, get_tasks

urlpatterns = [
    path('create-user/', create_user),
    path('tasks/', create_task, name='create-task'),
    path('tasks/<int:task_id>/assign/', assign_task, name='assign-task'),
    path('users/<int:user_id>/tasks/', get_tasks, name='user-tasks'),
]


    