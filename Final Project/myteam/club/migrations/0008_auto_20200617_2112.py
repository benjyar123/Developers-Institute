# Generated by Django 3.0.7 on 2020-06-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20200617_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='goals_against',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='goals_for',
            field=models.IntegerField(null=True),
        ),
    ]
