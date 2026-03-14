from django.db import models
from apps.user.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} | {self.author}"
    
