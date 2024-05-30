from django import forms
from . models import Course

class CourseFrom(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"