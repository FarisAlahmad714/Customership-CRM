from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

class Lead(models.Model):
    
    # SOURCE_CHOICES = (
    #     ('YT', 'Youtube')
    #     ('GL', 'Google')
    #     ('NL', 'Newsletter')
    # )
    
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent" , on_delete=models.CASCADE)
    # ONCASCADE IS GOING TO DELETE ALL LEADS UNDER AGENT DELETED, MOVE LEADS TO ANOTHER AGENT BEFORE DELETTION
    
    # contacted = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_lenght = 100)
    # profile_pic = models.ImageField(blank=True, null=True)
    # files = models.FileField(blank=True, null= True)
    