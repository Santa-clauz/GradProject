# Generated by Django 4.1.6 on 2023-03-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='capacity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
