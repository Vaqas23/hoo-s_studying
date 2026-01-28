from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.homeview, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='accounts:login'), name="logout"),
    path("signup/", views.signup, name="signup"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html", name="password_reset")),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html", name="password_reset_done")),
]
