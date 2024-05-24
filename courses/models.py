from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
