from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('home/', views.homeview, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='accounts:login'), name="logout"),
    path("signup/", views.signup, name="signup"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html",
        email_template_name="accounts/password_reset_email.txt",
        html_email_template_name="accounts/password_reset_email.html",
        success_url=reverse_lazy('accounts:password_reset_done')), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
