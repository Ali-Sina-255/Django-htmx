from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('file-list/', views.film, name='film')
]


htmx_urlpatterns  =  [
    path('check_username/', views.check_username, name='check_username')
]
urlpatterns += htmx_urlpatterns

