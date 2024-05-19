# Generated by Django 4.2 on 2024-05-19 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("films", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="film",
            options={"ordering": [django.db.models.functions.text.Lower("film")]},
        ),
        migrations.CreateModel(
            name="UserFilm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveSmallIntegerField()),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="films.film"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]