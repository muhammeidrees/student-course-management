from django.shortcuts import render
from .models import Course
from .forms import CourseForm
# Create your views here.
def create_course(request):
    form = CourseForm()
    
    if request.method == "POST":
        form = CourseForm(request.POST)
        
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            
            return redirect("course_list")
    return render(request,)