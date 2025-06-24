from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    role = [
        ('seeker','Seeker'),
        ('recuiter', 'Recuiter')
    ]
    user_type = models.CharField(choices=role, max_length=10, null=True)
