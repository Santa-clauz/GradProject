# Generated by Django 4.1.3 on 2022-11-27 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='event',
            name='left_capacity',
        ),
    ]
