# Generated by Django 2.2.4 on 2021-06-06 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_remove_rate_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]