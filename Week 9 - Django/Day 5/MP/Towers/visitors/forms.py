from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.models import User
from .models import Reservation
import datetime


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class AddReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["check_in", "check_out", "room"]
        labels = {
            "check_in": "Check in Date",
            "check_out": "Check out Date",
            "room": "Available Rooms",
        }

class AvailabilityCheck(Form):
        check_in = forms.DateField(initial=datetime.date.today)
        check_out = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=1))

