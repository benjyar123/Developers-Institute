# Generated by Django 3.0.6 on 2020-05-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0007_auto_20200524_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]