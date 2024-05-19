from django.db.models import Max
from . models import UserFilm

def get_max_order(user):
    existing_film = UserFilm.objects.filter(user=user)
    if not existing_film.exists():
        return 1
    else:
        current_max = existing_film.aggregate(max_order= Max('order'))['max_order']
        return current_max + 1
    


def reorder(user):
    existing_film = UserFilm.objects.filter(user=user)
    if not existing_film.exists():
        return 
    else:
        number_of_film = existing_film.count()
        new_ordering = range(1, number_of_film + 1)

    for order, user_film in zip(new_ordering,existing_film):
        user_film.order = order
        user_film.save()

