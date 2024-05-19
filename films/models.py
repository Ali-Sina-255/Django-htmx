from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower


class Film(models.Model):
    user = models.ManyToManyField(User, related_name='film', through='UserFilm')
    film = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='film-images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.film
    
    class Meta:
        ordering = [Lower('film')]

class UserFilm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']