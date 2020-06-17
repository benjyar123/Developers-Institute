from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import ComposeMessageForm, ComposeClubMessageForm, MessageUserForm
from .models import Message
from account.models import Club, Profile
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings



# Create your views here.

def compose_message(request):
    context = {
        'title': "Compose Message",
        'form': ComposeMessageForm(request.POST)
    }

    if request.method == 'POST':
        form = ComposeMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile
            message.save()
            send_mail(
                message.subject,
                f"Hello {message.receiver.first_name},\n\nYou are receiving this message because {message.sender.first_name} {message.sender.last_name} has contacted you using their MyTeam account. See their message below, and log in to your account to get more information about your team.\n\nThanks,\nMyTeam Admin\n\n----------------------------------\n\n {message.content}",
                'myteam.sports123@gmail.com',
                [message.receiver.email],
                fail_silently=False,
            )
            return redirect("profile")
    return render(request, "composemessage.html", context)


# This one not working
def message_user(request, profile_id):
    recipient = get_object_or_404(Profile, id=profile_id)
    context = {
        'title': "Compose Message",
        'form': MessageUserForm(request.POST),
        'recipient': recipient,
    }

    if request.method == 'POST':
        form = MessageUserForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile
            message.receiver = recipient
            message.save()
            send_mail(
                message.subject,
                f"Hello {message.receiver.first_name},\n\nYou are receiving this message because {message.sender.first_name} {message.sender.last_name} has contacted you using their MyTeam account. See their message below, and log in to your account to get more information about your team.\n\nThanks,\nMyTeam Admin\n\n----------------------------------\n\n {message.content}",
                'myteam.sports123@gmail.com',
                [message.receiver.email],
                fail_silently=False,
            )
            return redirect("profile")
    return render(request, "messageuser.html", context)



def compose_club_message(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Compose Club Message",
        'form': ComposeClubMessageForm(request.POST),
        'club': club,
    }
    if request.method == 'POST':
        form = ComposeClubMessageForm(request.POST)
        if form.is_valid():
            receiver_list = []
            for player in club.players.all():
                message = form.save(commit=False)
                message.receiver = player
                receiver_list.append(message.receiver.email)
                message.sender = request.user.profile
                message.pk = None
                message.save()

            send_mail(
                message.subject,
                f"Mesage to all {club.name} players;\n\nYou are receiving this message because {message.sender.first_name} {message.sender.last_name} has contacted you using their MyTeam account. See their message below, and log in to your account to get more information about your team.\n\nThanks,\nMyTeam Admin\n\n----------------------------------\n\n {message.content}",
                'myteam.sports123@gmail.com',
                receiver_list,
                fail_silently=False,
            )

            return redirect("profile")
    return render(request, "clubmessage.html", context)

def read_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    context = {
        'title': "Read Message",
        'heading': "Read Message",
        'message': message,
    }
    if message.status == 'Unread':
        message.status = 'Read'
        message.save()
    return render(request, "readmessage.html", context)

def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return redirect("profile")



