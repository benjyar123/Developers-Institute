from django.db import models
from account.models import Club, Profile
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Fixture(models.Model):

    # Initial setup

    HOME_AWAY_CHOICES = [
        ('Home', 'Home'),
        ('Away', 'Away'),
    ]
    COMPETITION_CHOICES = [
        ('League', 'League'),
        ('Cup', 'Cup'),
        ('Friendly', 'Friendly'),
    ]
    FORMATION_CHOICES = [
        ('4-4-2', '4-4-2'),
        ('4-3-3', '4-3-3'),
        ('4-5-1', '4-5-1'),
        ('5-3-2', '5-3-2'),
        ('Not Set', 'Not Set'),
    ]
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    opposition = models.CharField(default=None, max_length=100)
    home_away = models.CharField(choices=HOME_AWAY_CHOICES,  max_length=5)
    venue = models.CharField(default=None, max_length=100)
    competition = models.CharField(choices=COMPETITION_CHOICES, max_length=10)

    selected_team = models.ManyToManyField(Profile, related_name='selected_team', default=None)


class Result(models.Model):

    RESULT_CHOICES = [
        ('Win', 'Win'),
        ('Lose', 'Lose'),
        ('Draw', 'Draw'),
        ('N/A', 'N/A'),
    ]
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    result = models.CharField(default='N/A',choices=RESULT_CHOICES, max_length=5)
    goals_for = models.IntegerField(null=True)
    goals_against = models.IntegerField(null=True)

class PlayerAvailability(models.Model):
    AVAILABILITY_CHOICES = [
        ('Not Set', 'Not Set'),
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
        ('Maybe Available', 'Maybe Available'),
    ]
    player = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    availability = models.CharField(default='Not Set', choices=AVAILABILITY_CHOICES, max_length=20)

    def __str__(self):
        return (self.player.first_name + " " + self.player.last_name)


class PositionAssignment(models.Model):
    POSITION_CHOICES = [
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Attacker', 'Attacker'),
        ('Substitute', 'Substitute'),
        ('Not Set', 'Not Set'),
    ]
    player = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    position = models.CharField(default='Not Set', choices=POSITION_CHOICES, max_length=20)

    def __str__(self):
        return (self.player.first_name + " " + self.player.last_name)


class PlayerPerformance(models.Model):

    player = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    appearances = models.IntegerField(default=1)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    rating = models.IntegerField(default=0, null=True)




