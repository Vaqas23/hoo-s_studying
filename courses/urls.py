from django.urls import path
from . import views

urlpatterns = [
    path('my_courses/', views.my_courses, name="my_courses")
]
