from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default=None, max_length=20)
    last_name = models.CharField(default=None, max_length=20)
    birth_date = models.DateField(default=None)
    country = models.CharField(default=None, max_length=30)
    club = models.CharField(default=None, max_length=30)
    image = models.CharField(default=None, max_length=300)
    points = models.IntegerField(default=0)
    coins = models.IntegerField(default=100)




