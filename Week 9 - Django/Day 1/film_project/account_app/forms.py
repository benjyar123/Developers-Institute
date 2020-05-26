from django import forms
from django.forms import Form, ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.views.generic import CreateView

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]



