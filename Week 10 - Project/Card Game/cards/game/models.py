from django.db import models

class Player(models.Model):

    first_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(null=True, blank=True, max_length=30)
    position = models.CharField(null=True, blank=True, max_length=30)
    age = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(null=True, blank=True, max_length=30)
    team_name = models.CharField(null=True, blank=True, max_length=30)
    height = models.CharField(null=True, blank=True, max_length=10)
    weight = models.CharField(null=True, blank=True, max_length=10)
    appearances = models.IntegerField(null=True, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    passing_accuracy = models.IntegerField(null=True, blank=True)
    successful_dribbles = models.IntegerField(null=True, blank=True)
    tackles = models.IntegerField(null=True, blank=True)
    fouls_committed = models.IntegerField(null=True, blank=True)

    def price(self):
        if self.position == "Midfielder":
            appearances_value = (self.appearances + 1) / 15
            passing_value = (self.passing_accuracy + 1) / 12
            goals_value = ((self.goals + 1) / (self.appearances + 1)) * 5
            return round(appearances_value + passing_value + goals_value)

        elif self.position == "Defender":
            appearances_value = (self.appearances + 1)/ 10
            tackling_value = ((self.tackles + 1) / (self.appearances + 1)) * 4
            passing_value = (self.passing_accuracy + 1) / 20
            goals_value = ((self.goals + 1) / (self.appearances + 1)) * 5
            return round(appearances_value + tackling_value + passing_value + goals_value)

        elif self.position == "Attacker":
            appearances_value = (self.appearances + 1) / 10
            passing_value = (self.passing_accuracy + 1) / 17.5
            goals_value = ((self.goals + 1) / (self.appearances + 1)) * 15
            return round(appearances_value + passing_value + goals_value)

        elif self.position == "Goalkeeper":
            appearances_value = (self.appearances + 1) / 10
            passing_value = (self.passing_accuracy + 1) / 10
            return round(appearances_value + passing_value)
