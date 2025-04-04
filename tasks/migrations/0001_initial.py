# Generated by Django 5.1.7 on 2025-03-25 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('task_type', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress')], default='pending', max_length=50)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
