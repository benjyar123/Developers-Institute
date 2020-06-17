from django.forms import ModelForm
from .models import Message
from django.contrib.auth.models import User
from account.models import Profile


class ComposeMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["receiver", "subject", "content"]
        labels = {
            "receiver": "To:",
            "subject": "Subject:",
            "content": "Message:",
        }

class ComposeClubMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["subject", "content"]
        labels = {
            "subject": "Subject:",
            "content": "Message:",
        }

class MessageUserForm(ModelForm):
    class Meta:
        model = Message
        fields = ["subject", "content"]
        labels = {
            "subject": "Subject:",
            "content": "Message:",
        }