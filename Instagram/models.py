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

# User Posts
class Posts(models,Model):
    pic = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(blank=True,max_length=245)
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__ (self):
        return f'{self.Profile.user.username}'


# User Comments
class Comments(models.Model):
    Post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length=245)
    Comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    Count = models.IntegerField(default=0)

    def __str__ (self):
        return f'{self.username}'

                   



