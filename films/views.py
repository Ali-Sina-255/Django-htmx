from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator

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
    user_film = UserFilm.objects.prefetch_related('film').filter(user=request.user)
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
    user_film = UserFilm.objects.filter(user=request.user)

    results = Film.objects.filter(film__icontains=result_text).exclude(
        name__in = user_film.values_list('film__film', flat=True)
    )
    context = {
        "results":results
    }
    return render(request, 'partials/sreach-result.html',context)



def sort(request):
    film_pk_order = request.POST.getlist('film_order')
    print(film_pk_order)
    film = []
    updated_film = []
    user_film = UserFilm.objects.prefetch_related('film').filter(user=request.user)
    for index,film_pk in enumerate(film_pk_order, start=1):
        # user_film = UserFilm.objects.get(pk=film_pk)
        user_film = next(u for u in user_film if u.pk == int(film_pk))
        if user_film != index:
            user_film.order = index
            updated_film.append(user_film)

        user_film.append(user_film)
        # user_film.save()
    UserFilm.objects.bulk_update(user_film,['order'])
    
    context = {"films":film}
    return render(request, 'partials/film-list.html', context)

def detail_view(request,pk):
    user_films = get_object_or_404(UserFilm, pk=pk)
    paginator = Paginator(user_films, 3)
    page = request.GET.get('page')
    paged_all_user_film = paginator.get_page(page)
    context = {"user_films":paged_all_user_film}
    return render(request, 'partials/film-detail.html', context)


def film_list_partial_view(request):
    films = UserFilm.objects.filter(user=request.user)
    paginator = Paginator(films, 4)
    age_number = request.GET.get("page")
    paged_all_user_film = paginator.get_page(age_number)
  
    context = {
        "films":paged_all_user_film
    }
    return render(request, 'partials/film-list.html', context)


def upload_photo_view(request,pk):
    user_film = get_object_or_404(UserFilm, pk=pk)
    print(request.FILES)
    photo = request.FILES.get('photo')
    user_film.film.photo.save(photo.name, photo) 
    context = {
        "user_film":user_film
    }
    return render(request, 'partials/film-detail.html', context)