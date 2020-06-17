# Generated by Django 3.0.6 on 2020-05-20 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200520_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Category'),
        ),
    ]