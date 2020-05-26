from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignupForm, LoginForm
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

# class Signup(CreateView):
#     form_class = UserCreationForm
#     template_name = "signup.html"
#     success_url = "/login"
#
# class Login(FormView):
#     form_class = AuthenticationForm
#     template_name = "login.html"
#     success_url = "/homepage"

class Signup(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = "/login"

    def form_valid(self, form):
        out = super().form_valid(form)
        return out


# class Login(CreateView):
#     form_class = LoginForm
#     template_name = "login.html"
#     success_url = "/homepage"


def logout_view(request):
    logout(request)
    return redirect("login")


