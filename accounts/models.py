from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    # Having these declared variables makes it easy if we want to change anything later, as it will be reused
    YEAR_FRESHMAN = '1'
    YEAR_SOPHOMORE = '2'
    YEAR_JUNIOR = '3'
    YEAR_SENIOR = '4'
    YEAR_GRADUATE = 'G'

    YEAR_CHOICES = [
        # Django stores tuple position 0 in database and displays position 1
        (YEAR_FRESHMAN, '1st Year'),
        (YEAR_SOPHOMORE, '2nd Year'),
        (YEAR_JUNIOR, '3rd Year'),
        (YEAR_SENIOR, '4th Year'),
        (YEAR_GRADUATE, 'Graduate'),
    ]

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other / Prefer Not to Say'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    year = models.CharField(
        max_length=1, choices=YEAR_CHOICES, blank=True)
    majors_minors = models.CharField(max_length=200, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True)
    preferred_meeting_times = models.CharField(max_length=100, blank=True)
    preferred_meeting_location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
