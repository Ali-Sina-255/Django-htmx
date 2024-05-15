from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

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

@login_required(login_url='login')
def film(request):
    user_film = Film.objects.filter(user=request.user)
    context = {
        "films": user_film
    }
    return render(request, 'film/film.html', context)


@login_required(login_url='login')
def add_film(request):
    name = request.POST['filmname']
    film = Film.objects.create(film=name)
    # add the film to the user's list
    request.user.film.add(film)
    
    # return template with of all user's list
    films = request.user.film.all()
    context = {"films":films}
    return render(request, 'partials/film-list.html', context)


@login_required(login_url='login')
@require_http_methods(['DELETE'])
def delete_film_view(request, pk):
    # delete the user data
    request.user.film.remove(pk)
    film = request.user.film.all()
    context = {"films":film}
    return render(request, 'partials/film-list.html', context)

def search_film_view(request):
    result = request.POST.get('search')
    result = Film.objects.filter(film__icontains=result)
    context = {
        "result":result
    }
    return render(request, 'partials/film-list.html',context)


