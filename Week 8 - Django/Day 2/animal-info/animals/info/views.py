from django.shortcuts import render
from .models import Family
from .models import Animal

# Create your views here.
def index(request):
    return render(request, "index.html")

def family(request, family_id):
    this_family = Family.objects.get(id=family_id)
    return render(request, "family.html", {"family": this_family})

def animals(request):
    all_animals = Animal.objects.all()
    return render(request, "animals.html", {"all_animals": all_animals})

def animal(request, animal_id):
    this_animal = Animal.objects.get(id=animal_id)
    return render(request, "animal.html", {"animal": this_animal})