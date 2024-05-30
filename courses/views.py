from django.shortcuts import render
from . models import Course, Module
from .forms import CourseFrom


def course(request):
    courses = Course.objects.all()
    context  = {
        "courses":courses
    }
    return render(request, 'course/university.html',context)


def modules_view(request):
    course = request.GET.get("course")
    modules = Module.objects.filter(course=course)
    print(modules)
    context = {"modules":modules}
    return render(request, 'course/partials/modules.html',context) 

def add_new_view(request):
    if request.method == "POST":
        form = CourseFrom(request.POST)
        if form.is_valid():
            form.save()
            
   
    if request.htmx:
        all_course = Course.objects.all()
        return render(request, 'course/partials/add_new.html',{
        "all_course":all_course
    })

    else:
        form = CourseFrom()
    context = {"form":form}
    return render(request, 'course/add_new.html', context)


def course_list(request):
    all_course = Course.objects.all()
    return render(request, 'course/partials/add_new.html',{
        "all_course":all_course
    })
