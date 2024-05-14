from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')

def check_username(request):
    username = request.POST.get('username')
    print(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color:red">this username is already exists<div>')
    else:
        return HttpResponse('<div style="color:green"> this username is available<div>')