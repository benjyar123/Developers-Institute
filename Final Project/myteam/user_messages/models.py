from django.db import models

from django.db import models
from account.models import Profile

class Message(models.Model):
    STATUS_CHOICES = [
        ('Unread', 'Unread'),
        ('Read', 'Read'),
    ]

    sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="receiver", on_delete=models.CASCADE)
    subject = models.CharField(default=None, max_length=100)
    content = models.TextField(default=None, max_length=3000)
    status = models.TextField(default='Unread', choices=STATUS_CHOICES, max_length=100)
    time = models.DateField(auto_now=True)

