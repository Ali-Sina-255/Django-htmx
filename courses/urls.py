from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.course , name='course'),
    path('medule/', views.modules_view,name='modules')
]
