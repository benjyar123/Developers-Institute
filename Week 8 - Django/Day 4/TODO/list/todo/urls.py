from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
   path("", views.base, name="base"),
   path("todo", views.todo,name="todo"),
   path("signup", views.signup,name="signup"),
   path("login", views.login,name="login"),
]