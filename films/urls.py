from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('file-list/', views.film, name='film'),
]


htmx_urlpatterns  =  [
    path('check_username/', views.check_username, name='check_username'),
    path('add_film/', views.add_film, name='add_film'),
    path('delete-film/<int:pk>/', views.delete_film_view, name='delete_film'),
    path('search_film_view/', views.search_film_view, name='search_film_view'),
]
urlpatterns += htmx_urlpatterns

