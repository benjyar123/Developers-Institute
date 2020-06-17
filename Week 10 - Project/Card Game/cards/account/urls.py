from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("register", views.Register.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("profile", views.profile, name="profile"),
]
