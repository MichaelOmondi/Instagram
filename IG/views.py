from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Posts,Following,Comments
from .forms import DetailsForm,PostForm
from django.db.models import F

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')


@login_required(login_url='/acounts/login/')    
