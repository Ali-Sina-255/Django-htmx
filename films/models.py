from django.db import models
from django.contrib.auth.models import User



class Film(models.Model):
    user = models.ManyToManyField(User, related_name='film')
    film = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.film