from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    created_in_country = models.ForeignKey(Country, related_name="country_created", on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    image = models.CharField(null=True, max_length=300)
    director = models.ForeignKey(Director, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="film_reviews")


