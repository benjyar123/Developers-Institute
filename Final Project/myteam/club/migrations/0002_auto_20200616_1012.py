# Generated by Django 3.0.7 on 2020-06-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='formation',
            field=models.CharField(choices=[('4-4-2', '4-4-2'), ('4-3-3', '4-3-3'), ('4-5-1', '4-5-1'), ('5-3-2', '5-3-2'), ('Not Set', 'Not Set')], default='Not Set', max_length=10),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='instructions',
            field=models.TextField(default=None, max_length=3000, null=True),
        ),
    ]
