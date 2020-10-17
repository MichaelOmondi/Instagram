from django.db import models
from django.contrib.auth.models import User

# User Profile 
class Profile(models.Model):

    User = models.OneToOneField (User, on_delete=models.CASCADE)  
    Profile_pic = models.ImageField(blank=True,uplad_to = 'image/')
    bio = models.CharField(max_length=245)

    def __str__(self):
       return f'{self.user.username}'  
       
# User Following
class Following(models.Model):
    username = models.CharField(blank=True,max_length=245)
    followed = models.CharField(blank=True,max_length=245)

    def __str__(self):
        return f'{self.username}'



