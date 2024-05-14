from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from django.http import HttpResponse
from. models import Film


def index(request):
    return render(request, 'index.html')

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div id="username-error" class="success">this username is already exists<div>')
    else:
        return HttpResponse('<div id="username-error" class="error" > this username is available<div>')
    
    
def film(request):
    user_film = Film.objects.filter(user=request.user)
    context = {
        "films": user_film
    }
    return render(request, 'film/film.html', context)


def add_file(request):
    return render(request, 'add_film.html')