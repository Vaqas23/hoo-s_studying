from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.code


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student")
    email_verified = models.BooleanField(default=False)
    courses = models.ManyToManyField(
        Course, blank=True, related_name="students")

    def __str__(self):
        return self.user.username
