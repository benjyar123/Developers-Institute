from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("register", views.Register.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("profile", views.profile, name="profile"),
    path("profile/<profile_id>", views.otherprofile, name="otherprofile"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("clubregistration", views.clubregistration, name="clubregistration"),
#     path("about", views.about, name="about"),
#     path("register", views.Register.as_view(), name="register"),
#     path("login", LoginView.as_view(), name="login"),
#     path("logout_view", views.logout_view, name="logout_view"),
#     path("profile", views.profile, name="profile"),
]
