from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from verify_email.email_handler import EmailHandler


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # logs in immediately after signup
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})


def verify_email(token):
