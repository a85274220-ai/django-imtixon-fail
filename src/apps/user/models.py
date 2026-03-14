from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    telefon_raqam = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.username}"