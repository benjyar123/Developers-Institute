from django import forms
from django.forms import Form, ModelForm
from .models import User, Todo

class AddUser(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ToDoForm(ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        exclude = ["date_completion", "deadline_date"]

