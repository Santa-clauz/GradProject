# Generated by Django 4.1.6 on 2023-02-23 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='tenpogram',
            new_name='tempogram',
        ),
    ]
