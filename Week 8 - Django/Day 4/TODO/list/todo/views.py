from django.shortcuts import render, redirect
from .models import User
from .models import Todo
from .models import Category
from .forms import AddUser, ToDoForm


def base(request):
    return render(request, "base.html")

def todo(request):

    context = {
        'heading' : "To Do List",
        'form' : ToDoForm(),
        'jobs': Todo.objects.all()
    }
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'todo.html', context)



def login(request):
    return render(request, "login.html")

def signup(request):
    context = {
        'heading' : "Sign Up Page",
        'form' : AddUser()
    }
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base.html', context)

    return render(request, 'signup.html', context)

