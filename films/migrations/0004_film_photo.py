# Generated by Django 4.2 on 2024-05-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("films", "0003_alter_film_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="film-images/"),
        ),
    ]