# Generated by Django 5.1.1 on 2024-09-05 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='info',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='info',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='info',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='info',
        ),
    ]
