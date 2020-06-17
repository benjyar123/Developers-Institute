from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("signup", views.Signup.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout_view", views.logout_view, name="logout_view"),
    # path("profile/<int:id>", views.profile, name="profile"),
    # remember to check settings in main project folder for login stuff at the bottom
]
