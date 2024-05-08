from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page is set up')
    # return render(request, '')