from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Course
from .forms import EnrollCourseForm

# Create your views here.


@login_required
def my_courses(request):
    student = request.user.student
    if request.method == "POST":
        form = EnrollCourseForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['course_code']
            course1 = Course.objects.get(code=code)
            student.courses.add(course1)
            return redirect('my_courses')
    else:
        form = EnrollCourseForm()

    return render(request, "courses/my_courses.html", {"form": form, "student": student})
