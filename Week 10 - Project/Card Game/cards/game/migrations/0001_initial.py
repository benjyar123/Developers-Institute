# Generated by Django 3.0.6 on 2020-06-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('position', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=30, null=True)),
                ('team_name', models.CharField(blank=True, max_length=30, null=True)),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('appearances', models.IntegerField(blank=True, null=True)),
                ('goals', models.IntegerField(blank=True, null=True)),
                ('passing_accuracy', models.IntegerField(blank=True, null=True)),
                ('successful_dribbles', models.IntegerField(blank=True, null=True)),
                ('tackles', models.IntegerField(blank=True, null=True)),
                ('fouls_committed', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]