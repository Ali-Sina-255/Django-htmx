from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.course , name='course'),
    path('medule/', views.modules_view,name='modules'),
    path('add-course/', views.add_new_view, name='add_new'),
    path('all_course/', views.course_list, name='course_list'),
]
