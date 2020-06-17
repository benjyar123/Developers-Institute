from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Player', 'Player'),
        ('Player-Manager', 'Player-Manager'),
    ]
    POSITION_CHOICES = [
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Attacker', 'Attacker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default=None, null=True, max_length=30)
    last_name = models.CharField(default=None, null=True, max_length=30)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default=None, null=True)
    position = models.CharField(choices=POSITION_CHOICES, max_length=12, default=None, null=True)
    email = models.EmailField(default=None, null=True)
    phone = models.IntegerField(default=None, null=True)
    image = models.ImageField(upload_to='gallery',default='gallery/football.png', null=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return (self.first_name + " " + self.last_name)
        else:
            return self.user.username

class Club(models.Model):
    name = models.CharField(default=None, max_length=50)
    logo = models.ImageField(null=True)
    manager = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='manager')
    players = models.ManyToManyField(Profile)
    password = models.CharField(max_length=20)









