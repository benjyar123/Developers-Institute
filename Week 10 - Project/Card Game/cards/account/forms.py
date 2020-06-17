from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
from .models import Profile
import datetime


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "birth_date", "country", "club", "image"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "birth_date": "Birth Date",
            "country": "Country of Origin",
            "club": "Favourite Team",
            "image": "Image URL",
        }


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
