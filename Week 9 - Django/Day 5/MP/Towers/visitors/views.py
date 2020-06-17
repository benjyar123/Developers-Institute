from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import AddReservationForm, AvailabilityCheck
from .models import Room, Reservation
from django.utils.dateparse import parse_date
from datetime import timedelta, datetime

# Create your views here.

def home(request):
    context = {
        'title': "Home",
        'heading': "Welcome to Torquay Towers",
        'summary': "The worst hotel in England.",
    }
    return render(request, "home.html", context)

def info(request):
    context = {
        'title': "Information",
        'heading': "About Torquay Towers",
        'summary': "Rooms, rates, pics, etc.",
    }
    return render(request, "info.html", context)

def reservations(request):
    context = {
        'title': "Reservations",
        'heading': "Check Availability",
        'summary': "Which dates would you like to visit?",
        'form': AvailabilityCheck(),
        'rooms': Room.objects.all(),
        'reservations': Reservation.objects.all(),
    }
    if request.method == 'POST':
        form = AvailabilityCheck(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            nights = (check_out - check_in).days
            # request.session["check_in"] = check_in.strftime("%d-%b-%Y")
            # request.session["check_out"] = check_out.strftime("%d-%b-%Y")
            # 1) Find all reservations where dates are between requested check in and check out
            # 2) Find all rooms that appears in that filtered list of reservations, and remove them
            rooms = Room.objects.exclude(reservation__check_in__range=[check_in, check_out]).exclude(reservation__check_out__range=[check_in, check_out])
            print(rooms.query)
            context = {
                'title': "Availability",
                'heading': "Availability",
                'summary': "Choose a room",
                'rooms': rooms,
                'nights': nights,
                'check_in': str(check_in),
                'check_out': str(check_out),
            }
            return render(request, "availability.html", context)

    return render(request, "reservations.html", context)





def confirm(request, check_in, check_out, room_id):
    check_in = parse_date(check_in)
    check_out = parse_date(check_out)
    nights = check_out - check_in
    room = Room.objects.get(id=room_id)
    price = (nights.days) * room.rate
    context = {
        'title': "Booking Confirmation",
        'heading': "Booking Confirmation",
        'summary': "Your booking summary:",
        'form': AddReservationForm({'check_in': check_in, 'check_out': check_out, 'room': room_id}),
        'room': Room.objects.get(id=room_id),
        'nights': nights.days,
        'price': price,
    }
    if request.method == 'POST':
        form = AddReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return render(request, "home.html", context)

    return render(request, "confirm.html", context)




class Register(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "registration/login.html"

    def form_valid(self, form):
        out = super().form_valid(form)
        return out




def logout_view(request):
    logout(request)
    return redirect("login")