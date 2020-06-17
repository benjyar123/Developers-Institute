from django.forms import ModelForm, Form
from django import forms
from .models import Profile, Club

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "role", "position", "email", "phone", "image"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "role": "Role",
            "position": "Position",
            "email": "Email Address",
            "phone": "Phone Number",
            "image": "Upload your profile picture",
        }

class RegisterClubForm(ModelForm):
    class Meta:
        model = Club
        exclude = ['players', 'manager']


class RegisterPlayerForm(Form):
    fields = ["Club", "Password"]
    labels = {
        "club": "Club",
        "password": "Password",
    }



