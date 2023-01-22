from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='users')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    


class Music(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50) 
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lyrics = models.TextField()
    music = models.FileField(upload_to='musics/', null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='musics')
    chroma_stft = models.FloatField()
    spectral_centroid = models.FloatField()
    spectral_bandwidth = models.FloatField()
    rolloff = models.FloatField()
    zero_crossing_rate = models.FloatField()
    mfcc = models.FloatField()
    contrast = models.FloatField()
    tempo = models.FloatField()
    chroma_cqt = models.FloatField()
    chroma_cens = models.FloatField()
    melspectrogram = models.FloatField()
    poly_features = models.FloatField()
    tonnetz = models.FloatField()
    rms = models.FloatField()
    

class Rate(models.Model):
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rates')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='rates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Platlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    musics = models.ManyToManyField(Music, related_name='playlists')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')