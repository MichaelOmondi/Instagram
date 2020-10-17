from django.db import models
from django.contrib.auth.models import User

#Profile section
class Profile(models.Model):

    User = models.OneToOneField (User, on_delete=models.CASCADE)  
    Profile_pic = models.ImageField(blank=True,uplad_to = 'image/')
    bio = models.CharField(max_length=245)  

