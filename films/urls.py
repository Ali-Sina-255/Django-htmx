from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('check_username/', views.check_username, name='check_username')
   
]

