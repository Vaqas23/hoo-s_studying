from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Course
from .forms import EnrollCourseForm

# Create your views here.


@login_required
def my_courses(request):
    request = request.user.student
    if request.method == "POST":
        form = EnrollCourseForm(request.POST)
        if form.is_valid():
            # form.course_code
            return redirect('my_courses')
    else:
        form = EnrollCourseForm()

    return render(request, "accounts/signup.html", {"form": form})
