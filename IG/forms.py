from .models import Profile,Posts
from django import forms

#Form
class DetailsForm(forms,ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile','date','like']

        
                