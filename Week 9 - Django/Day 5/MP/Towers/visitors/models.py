from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Room(models.Model):
    beds = models.IntegerField()
    rate = models.IntegerField()
    img_url = models.CharField(default="https://pix10.agoda.net/hotelImages/123/1235585/1235585_17091311590056285210.jpg?s=1024x768", max_length=300)
    category = models.CharField(default="Standard", max_length=20)

class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





