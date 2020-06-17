from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=150)
    manager = models.ForeignKey(User)
    players = models.ManyToManyField(User)
    home_ground = models.CharField(max_length=150)



class Player(models.Model):
    first_name = models.CharField(max_length=150)
    availability = models.ManyToManyField(Fixture)


class Fixture(models.Model):
    date = models.DateField()
    venue = models.CharField(max_length=100)
    home =
    result =
    opposition =

class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_team")
    away_team = models.ForeignKey(Team, related_name="away_team")




