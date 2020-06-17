from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib import admin

urlpatterns = [
    path("home", views.home, name="home"),
    path("info", views.info, name="info"),
    path("register", views.Register.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("reservations", views.reservations, name="reservations"),
    path("confirm/<check_in>/<check_out>/<room_id>", views.confirm, name="confirm"),

]
