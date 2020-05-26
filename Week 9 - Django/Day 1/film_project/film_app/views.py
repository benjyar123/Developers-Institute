from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddDirectorForm, AddFilmForm, AddReviewForm
from .models import Film, Director
from django.views import generic


# Create your views here.

def addFilm(request):
    context = {
        'title': "Add Film",
        'heading': "Add Film",
        'summary': "Add Film Form goes here.",
        'form': AddFilmForm(),
    }
    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "film/addFilm.html", context)

def addDirector(request):
    context = {
        'title': "Add Director",
        'heading': "Add Director",
        'summary': "Add Director Form goes here.",
        'form': AddDirectorForm(),
    }
    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "director/addDirector.html", context)

def homepage(request):
    context = {
        'title': "Home Page",
        'heading': "IMDI Home Page",
        'summary': "Browse our movie database.",
        'films': Film.objects.all(),
        'form': AddReviewForm(),
    }
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        film_id = int(request.POST.get("film_id"))
        if not Film.objects.filter(id=film_id).exists():
            return redirect("homepage")
        film = Film.objects.get(id=film_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.film = film
            review.save()
    return render(request, "homepage.html", context)


def editDirector(request, id):
    instance = get_object_or_404(Director, id=id)
    context = {
        'title': "Edit Director Details",
        'heading': "Edit Director Details",
        'summary': "Edit Director Form",
        'form': AddDirectorForm(request.POST or None, instance=instance)
    }
    if request.method == 'POST':
        form = AddDirectorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, "director/editDirector.html", context)

def editFilm(request, id):
    instance = get_object_or_404(Film, id=id)
    context = {
        'title': "Edit Film Details",
        'heading': "Edit Film Details",
        'summary': "Edit Director Form",
        'form': AddFilmForm(request.POST or None, instance=instance)
    }
    if request.method == 'POST':
        form = AddFilmForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, "film/editFilm.html", context)







