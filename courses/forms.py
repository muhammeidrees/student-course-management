from django import forms
from .model import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["title","description"]