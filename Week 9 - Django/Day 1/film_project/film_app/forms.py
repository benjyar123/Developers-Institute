from django import forms
from django.forms import *
from .models import Film, Director, Review
from django.views.generic import CreateView

class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets = {"category": CheckboxSelectMultiple}

class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"

class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]




