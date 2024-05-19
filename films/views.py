from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse
from. models import Film,UserFilm
from . utils import get_max_order, reorder
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
    user_film = UserFilm.objects.filter(user=request.user)
    context = {
        "films": user_film
    }
    return render(request, 'film/film.html', context)


@login_required(login_url='login')
def add_film(request):
    name = request.POST['filmname']
    film = Film.objects.get_or_create(film=name)[0]
    # add the film to the user's list
    
    if not UserFilm.objects.filter(film=film,user=request.user).exists():
        UserFilm.objects.create(film=film, user=request.user, order=get_max_order(request.user))
    # return template with of all user's list
    films = UserFilm.objects.filter(user=request.user)

    context = {"films":films}
    return render(request, 'partials/film-list.html', context)


@login_required(login_url='login')
@require_http_methods(['DELETE'])
def delete_film_view(request, pk):
    # delete the user data
    UserFilm.objects.get(pk=pk).delete()
    reorder(request.user)
    # request.user.film.remove(pk)
    film = UserFilm.objects.filter(user=request.user)
    context = {"films":film}
    return render(request, 'partials/film-list.html', context)


def search_film_view(request):
    result_text = request.POST.get('search')
    userfilm = UserFilm.objects.filter(user=request.user)

    results = Film.objects.filter(film__icontains=result_text).exclude(
        name__in = userfilm.values_list('film__film', flat=True)
    )
    context = {
        "results":results
    }
    return render(request, 'partials/sreach-result.html',context)



def sort(request):
    film_pk_order = request.POST.getlist('film_order')
    print(film_pk_order)
    film = []
    for index,film_pk in enumerate(film_pk_order, start=1):
        userfile = UserFilm.objects.get(pk=film_pk)
        userfile.order = index
        userfile.save()
        film.append(userfile)
    context = {"films":film}
    return render(request, 'partials/film-list.html', context)