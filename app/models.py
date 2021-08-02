from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class User(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email   = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

class Blog(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)



def __str__(self):
    return self.title

    

       

# Create your models here.


# Create your models here.
