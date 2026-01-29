from django.urls import path
from . import views

app_name = "courses"
urlpatterns = [
    path('my_courses/', views.my_courses, name="my_courses")
]
