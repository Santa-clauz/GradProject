from django.db import models
from django.db.models.fields import DateField
from login_registeration_app.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Music(models.Model):
    song_name=models.CharField(max_length=45)
    writer=models.CharField(max_length=45)
    composer = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lyrics=models.TextField()
    music = models.FileField(upload_to='audio/', blank=True)
    uploaded_by=models.ForeignKey(User,related_name="songs",on_delete=models.CASCADE)
    

class Rate(models.Model):
    music=models.ForeignKey(Music,related_name="rates",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="rates",on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )


class Event(models.Model):
    name=models.CharField(max_length=45)
    date=models.DateField()
    time=models.TimeField()
    image = models.ImageField(upload_to='images/',default='pic.png')
    location=models.CharField(max_length=45)
    creator=models.ForeignKey(User,related_name="events",on_delete=models.CASCADE)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attendees=models.ManyToManyField(User,related_name="attending")
    price=models.IntegerField()

    

class Ticket(models.Model):
    event=models.ForeignKey(Event,related_name="tickets",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="tickets",on_delete=models.CASCADE)
    price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    name=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',default='pic.png')
    songs=models.ManyToManyField(Music,related_name="albums")
    uploaded_by=models.ForeignKey(User,related_name="albums",on_delete=models.CASCADE)

class PlayList(models.Model):
    name=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    songs=models.ManyToManyField(Music,related_name="playlists")
    uploaded_by=models.ForeignKey(User,related_name="playlists",on_delete=models.CASCADE)