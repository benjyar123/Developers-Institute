# Generated by Django 3.0.6 on 2020-05-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20200528_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(default='Standard', max_length=20),
        ),
        migrations.AddField(
            model_name='room',
            name='img_url',
            field=models.CharField(default='https://pix10.agoda.net/hotelImages/123/1235585/1235585_17091311590056285210.jpg?s=1024x768', max_length=300),
        ),
    ]