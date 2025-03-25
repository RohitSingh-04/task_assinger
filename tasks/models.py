from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STAUTS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress')]

    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices = STAUTS_CHOICES, default="pending")
    assignee = models.ManyToManyField(User, related_name='tasks')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name +" - "+ self.status