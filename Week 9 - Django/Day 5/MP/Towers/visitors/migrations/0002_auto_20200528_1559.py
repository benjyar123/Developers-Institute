# Generated by Django 3.0.6 on 2020-05-28 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='nights',
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(default=datetime.date(2020, 5, 31)),
            preserve_default=False,
        ),
    ]