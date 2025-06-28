from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    fullname = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    img = models.ImageField(upload_to='Media/profile')
    bio = models.TextField(max_length=200, null=True)
    password = models.CharField()


class TaskModel(models.Model):
    TaskTitle = models.CharField(max_length=200)
    TaskDescription = models.TextField(max_length=200)
    TaskPriority = models.CharField(max_length=50)
    TaskStatus = models.CharField(max_length=50)
    TaskDueDate = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)