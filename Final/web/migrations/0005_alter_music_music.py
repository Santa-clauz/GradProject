# Generated by Django 4.1.6 on 2023-02-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_remove_music_heirarchical_cluster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.FileField(blank=True, max_length=512, null=True, upload_to='musics/'),
        ),
    ]
