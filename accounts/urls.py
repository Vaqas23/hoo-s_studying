from django.urls import path
from .views import edit_profile

urlpatterns = [
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/', profile_detail, name='profile_detail'),
]
