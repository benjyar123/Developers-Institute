# Generated by Django 3.0.6 on 2020-05-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0010_auto_20200526_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
