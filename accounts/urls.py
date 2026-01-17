from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import edit_profile, personal_profile_detail, other_profile_detail

app_name = "accounts"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('profile/me/', personal_profile_detail, name='my_profile_view'),
    path('profile/me/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', other_profile_detail, name='user_profile_view'),
]
