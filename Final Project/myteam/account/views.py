from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import CreateProfileForm, RegisterClubForm, RegisterPlayerForm
from .models import Profile, Club
from user_messages.models import Message
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {
        'title': "Home",
        'heading': "Welcome to MyTeam",
        'summary': "Site for all amateur football team needs.",
    }
    return render(request, "home.html", context)

def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)
    context = {
        'title': "Profile",
        'heading': "Profile Page",
        'clubs': Club.objects.filter(manager=request.user.profile),
        'player_clubs': Club.objects.filter(players=request.user.profile),
        'user_messages': Message.objects.filter(receiver=request.user.profile),
        'num_unread_messages': Message.objects.filter(receiver=request.user.profile, status='Unread').count(),
        'sent_messages': Message.objects.filter(sender=request.user.profile),
        'form': CreateProfileForm(),
    }
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = profile
            profile.save()
            return render(request, "profile.html", context)

    return render(request, "profile.html", context)

def otherprofile(request, profile_id):
    player = get_object_or_404(Profile, id=profile_id)
    if request.user.id == player.user.id:
        return redirect("profile")
    else:
        context = {
            'title': "Someone Else Profile",
            'heading': "Someone Else Profile",
            'player': player,
            'player_clubs': Club.objects.filter(players=player.user.profile),
        }
        return render(request, "otherprofile.html", context)


def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'title': "Edit Profile Details",
        'heading': "Edit Profile",
        'profile': profile,
        'form': CreateProfileForm(request.POST or None, instance=profile)
    }
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    return render(request, "editprofile.html", context)


def clubregistration(request):
    context = {
        'title': "Register Club",
        'heading': "Register Your Team",
        'form': RegisterClubForm(),
    }
    if request.method == 'POST':
        form = RegisterClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.manager = request.user.profile
            club.save()
            return render(request, "profile.html", context)

    return render(request, "clubregistration.html", context)



def clubs(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Club Details",
        'heading': club.name,
        'club': club,
    }
    return render(request, "clubdetails.html", context)



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