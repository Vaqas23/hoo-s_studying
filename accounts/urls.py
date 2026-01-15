from django.urls import path
import django.contrib.auth.urls
from .views import edit_profile, personal_profile_detail, other_profile_detail

app_name = "accounts"

urlpatterns = [
    path('profile/me/', personal_profile_detail, name='my_profile_view'),
    path('profile/me/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', other_profile_detail, name='user_profile_view'),
]
