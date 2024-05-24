from django.core.management.base import BaseCommand
from courses.models import Course, Module

class Command(BaseCommand):
    help = "Load Courses and Modules"
    def handle(self, *args, **kwargs):
        Module.objects.all().delete()
        course_names = ["Computer Science", "Mathematics", "Physic", "Film Studios"]

        if not Course.objects.count():
            for course_name in course_names:
                Course.objects.create(name=course_name)

        # Computer Since
        cs = Course.objects.get(name="Computer Science")

        compcsi_modules = [
            "AI",
            "Machine Learning",
            "Web Development",
            "SoftWear Engineering",
            "No SQL Databases",
        ]

        for module in compcsi_modules:
            Module.objects.create(name=module, course=cs)

        math = Course.objects.get(name="Mathematics")
        math_module = [
            "Linear Algebra",
            "Differential Equations",
            "Graph Theory",
            "Topology",
            "numbers Theory",
        ]
        Module.objects.create(name=module, course=math)

    
        physic = Course.objects.get(name='Physic')
        physic_modules = [
            'Quantum, Mechanism',
            'Optics',
            "Astronomy","Solid State Physic","Electrmagetic Theory"
        ]
        for module in physic_modules:
            Module.objects.create(name=module, course=physic)
        
        film = Course.objects.get(name='Film Studios')
        film_module = ["Film Noir","Slilned filme","Fist the word Film","98"]

        for module in film_module:
            Module.objects.create(name=module,course=film)