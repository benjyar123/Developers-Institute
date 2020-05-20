from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=500)
    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True)
    deadline_date = models.DateField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)


