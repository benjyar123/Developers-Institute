# Generated by Django 3.0.6 on 2020-06-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='coins',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]