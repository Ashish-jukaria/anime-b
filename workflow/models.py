from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password= models.CharField(max_length=255)
    
class UserPrefrence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prefrence = ArrayField(models.CharField(max_length=255))