# Generated by Django 4.2 on 2024-05-19 10:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("films", "0002_alter_film_options_userfilm"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="user"
        ),
        migrations.AddField(
            model_name='film',
            name='user',
            field=models.ManyToManyField(
                related_name="film",
                through="films.UserFilm",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
