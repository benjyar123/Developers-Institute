# Generated by Django 3.0.6 on 2020-05-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
