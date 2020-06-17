from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import EditProfileForm
from .models import Profile
from game.models import Player

# Create your views here.

def home(request):
    context = {
        'title': "Home",
        'heading': "Welcome to card trading game",
        'summary': "Where you can trade football cards",
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        'title': "About",
        'heading': "About",
        'summary': "What is this site then?",
        'players': (Player.objects.order_by('team_name', 'position', 'last_name', 'first_name'))
    }
    return render(request, "about.html", context)

def profile(request):
    context = {
        'title': "Profile",
        'heading': "Profile Page",
        'summary': "This is where a user can see their profile and edit details or something",
        'form': EditProfileForm(),
    }
    if request.method == 'POST':
        try:
            form = EditProfileForm(instance=request.user.profile, data=request.POST)
        except:
            form = EditProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, "profile.html", context)

    return render(request, "profile.html", context)
















class Register(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "login"

    def form_valid(self, form):
        out = super().form_valid(form)
        return out

def logout_view(request):
    logout(request)
    return redirect("home")