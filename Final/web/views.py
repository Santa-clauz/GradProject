import requests
import numpy as np
import pandas as pd
from scipy import spatial
from web.models import *
from django.shortcuts import render, redirect
import bcrypt
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
from time import strftime
import stripe
from django.conf import settings
from django.core.paginator import Paginator
import random
import librosa
import librosa.display
import matplotlib.pyplot as plt
from librosa import feature
import numpy as np
import pandas as pd
import pickle
import joblib
import sys
# sys.modules['sklearn.externals.joblib'] = joblib
ss = joblib.load('media/models/minmax_scaler.bin')
kmeansModel = joblib.load('media/models/c_kmenas25.sav')
fn_list_i = [
    feature.chroma_stft,
    feature.spectral_centroid,
    feature.spectral_bandwidth,
    feature.spectral_rolloff,
    feature.spectral_contrast,
    feature.tempogram,
    feature.chroma_cqt,
    feature.chroma_cens,
    feature.melspectrogram,
    feature.mfcc,
    feature.poly_features,
    feature.tonnetz,
]
fn_list_ii = [
    feature.rms,
    feature.zero_crossing_rate
]


def get_feature_vector(y, sr):
    feat_vect_i = [np.mean(funct(y, sr)) for funct in fn_list_i]
    feat_vect_ii = [np.mean(funct(y)) for funct in fn_list_ii]
    feature_vector = feat_vect_i + feat_vect_ii
    return feature_vector


def featureExtraction(audio_path):
    y, sr = librosa.load(audio_path, mono=True)
    print(y, sr)
    feature_vector = get_feature_vector(y, sr)
    return feature_vector


header = ["chroma_stft",
          "spectral_centroid",
          "spectral_bandwidth",
          "spectral_rolloff",
          "spectral_contrast",
          "tempogram",
          "chroma_cqt",
          "chroma_cens",
          "melspectrogram",
          "mfcc",
          "poly_features",
          "tonnetz", "rms", "zero_crossing_rate"]


def musicadd(req):
    if req.method == 'POST':
        print(req.POST)
        print(req.FILES)
        path = req.FILES['music']
        songStats = featureExtraction(path)
        scaledStats = ss.transform([songStats])
        kmeansCluster = kmeansModel.predict(scaledStats)[0]
        print(kmeansCluster)

        user = User.objects.get(id=req.session['user_id'])
        music = Music.objects.create(
            name=req.POST['name'],
            music=req.FILES['music'],
            uploaded_by=user,
            chroma_stft=scaledStats[0][0],
            spectral_centroid=scaledStats[0][1],
            spectral_bandwidth=scaledStats[0][2],
            spectral_rolloff=scaledStats[0][3],
            spectral_contrast=scaledStats[0][4],
            tempogram=scaledStats[0][5],
            chroma_cqt=scaledStats[0][6],
            chroma_cens=scaledStats[0][7],
            melspectrogram=scaledStats[0][8],
            mfcc=scaledStats[0][9],
            poly_features=scaledStats[0][10],
            tonnetz=scaledStats[0][11],
            rms=scaledStats[0][12],
            zero_crossing_rate=scaledStats[0][13],
            kmean_cluster=kmeansCluster

        )
        music.save()
        return redirect('/')
    return render(req, 'artist/musicadd.html')


def create_song(req):
    return render(req, 'artist/create_song.html')


def recommendMusic(id):
    song = Music.objects.get(id=id)
    cluster = song.kmean_cluster
    features = [song.chroma_stft, song.spectral_centroid, song.spectral_bandwidth,
                song.spectral_rolloff, song.spectral_contrast, song.tempogram, song.chroma_cqt,
                song.chroma_cens, song.melspectrogram, song.mfcc, song.poly_features, song.tonnetz,
                song.rms, song.zero_crossing_rate]
    query = Music.objects.filter(kmean_cluster=cluster)
    rankingDf = pd.DataFrame.from_records(query.values())
    rankingDf["scores"] = rankingDf[header].apply(
        lambda x: spatial.distance.cosine(x, features), axis=1)
    rankingDf = rankingDf.sort_values(by=['scores'], ascending=True)
    rankingDf = rankingDf[:20]
    rankingDf = rankingDf[rankingDf['id'] != id]

    ids = rankingDf['id'].tolist()
    random.shuffle(ids)
    recommendations = Music.objects.filter(id__in=ids[:15])
    lastset = {}
    for i in recommendations:
        lastset.push(i)
    return lastset

def landing_page(request):
    return render(request, 'landing_page.html')


def artists(request):
    artists = User.objects.filter(role=2)
    p = Paginator(artists, 12)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    print(page)
    context = {
        'all': page,
    }
    return render(request, 'artist/artist1.html', context)


def eventadd(req):
    if req.method == 'POST':
        user = User.objects.get(id=req.session['user_id'])
        event = Event.objects.create(
            name=req.POST['name'],
            date=req.POST['date'],
            image=req.FILES['image'],
            description=req.POST['description'],
            location=req.POST['location'],
            creator=user,
            price=req.POST['price'],
            capacity=req.POST['capacity'],
        )
        event.save()
        return redirect('/')
    return render(req, 'artist/eventadd.html')


def blog(request):
    return render(request, 'blog.html')


def create_music(request):
    return render(request, 'create_music.html')


def create_playlist(request):
    return render(request, 'create_playlist.html')


def create_Event(request):
    return render(request, 'artist/create_event.html')


def Events(request):
    events = Event.objects.all()
    p = Paginator(events, 3)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    print(page)
    context = {
        'all': page,
    }
    return render(request, 'Events.html', context)


def adminallusers(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        if request.session['user_role'] == 1:
            users = User.objects.all()
            context = {
                'all': users,
            }
            return render(request, 'admin/adminallusers.html', context)
        else:
            return redirect('/')


def adminallmusic(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        if request.session['user_role'] == 1:
            musics = Music.objects.all()
            context = {
                'all': musics,
            }
            return render(request, 'admin/adminallmusic.html', context)
        else:
            return redirect('/')


def adminallevents(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        if request.session['user_role'] == 1:
            events = Event.objects.all()
            context = {
                'all': events,
            }
            return render(request, 'admin/adminallevents.html', context)
        else:
            return redirect('/')


def adminallartists(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        if request.session['user_role'] == 1:
            artists = User.objects.filter(role=2)
            context = {
                'all': artists,
            }
            return render(request, 'admin/adminallartists.html', context)
        else:
            return redirect('/')


def artist(request, id):
    artist = User.objects.get(id=id)
    music = Music.objects.filter(uploaded_by=artist.id)
    context = {
        'artist': artist,
        'music': music,
    }
    return render(request, 'artist/artistProfile.html', context)


def playlist(request):
    # playlist = Playlist.objects.get(id=id)
    # context = {
    #     'playlist': playlist,
    # }
    return render(request, 'playlist.html')


def music(request, id):
    music = Music.objects.get(id=id)
    k = music.name.split("(")
    music.name = k[0]
    recommendMusic(id)
    all = Music.objects.filter(uploaded_by=music.uploaded_by)[0:6]
    for i in all:
        g = i.name.split("(")
        i.name = g[0]
    context = {
        'i': music,
        'all': all,
    }
    return render(request, 'artist/player.html', context)


def login(request):
    print("login l7al222")
    return render(request, 'login.html')


def Login(request):
    print("login l7al")
    return render(request, 'Login.html')
stripe.api_key = settings.STRIPE_SECRET_KEY


def buy(request,id):
    event = Event.objects.get(id=id)
    ticket = Ticket.objects.create(
        event=event,
        user=request.user,
        price=event.price,
    )
    ticket.save()
    
    if request.method == 'POST':
        # Get the token from the form data
        token = request.POST.get('stripeToken')

        # Charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=event.price * 100,  # Amount in cents
                currency='usd',
                description='Example charge',
                source=token,
            )
        except stripe.error.CardError as e:
            # The card was declined
            pass

        # Render a success page
        return render(request, 'success.html')

    # Render the checkout page
    return render(request, 'checkout.html')


def loginP(req):
    redirect('/login')
    req.session.clear()
    user = User.objects.filter(email=req.POST['Email'])
    print(user)
    password = req.POST['password']
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            req.session['user_id'] = logged_user.id
            req.session['user_name'] = logged_user.username
            req.session['user_role'] = logged_user.role.id
            return redirect('/')
        else:

            req.session['wrong_password'] = "Please Check Password"
            return redirect('/shitpassword')
    else:
        req.session['wrong_username'] = "Please Check Username"
        return redirect('/shituser')


def register(req):
    clearify()
    gender_id = req.POST['gender']
    user_gender = Gender.objects.get(id=gender_id)
    x = req.FILES.get('upload')
    print(x)
    testzz = req.FILES['upload']
    user = User.objects.create(
        username=req.POST['username'],
        email=req.POST['email'],
        password=bcrypt.hashpw(
            req.POST['password'].encode(), bcrypt.gensalt()).decode(),
        birthdate=req.POST['birthdate'],
        phone=req.POST['phone'],
        address=req.POST['address'],

        role=Role.objects.get(id=3),

        gender=user_gender,
        image=x
    )
    return redirect('/')


def acceptartist(request, id):
    user_id = id
    user = User.objects.get(id=user_id)
    user.role = Role.objects.get(id=2)
    user.save()
    return redirect('/admin')


def declineartist(request, id):
    user_id = id
    user = User.objects.get(id=user_id)
    user.role = Role.objects.get(id=3)
    user.save()
    return redirect('/admin')


def test(req):
    return render(req, 'test.html')


def About(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact.html')


def logout(request):
    request.session.clear()
    return redirect('/')


def Show_events(request):
    return render(request, 'show_events.html')


def player(request):
    return render(request, 'player.html')


def registration(request):
    return render(request, 'registration.html')


def new(request):
    return render(request, 'Newest.html')


def admin_login(request):
    if 'user_id' in request.session:
        if request.session['user_role'] == 1:
            music_count = Music.objects.all().count()
            artist_count = User.objects.filter(role=2).count()
            event_count = Event.objects.all().count()
            user_count = User.objects.filter(role=3).count()
            admin_count = User.objects.filter(role=1).count()
            context = {
                'admin_count': admin_count,
                'music_count': music_count,
                'artist_count': artist_count,
                'event_count': event_count,
                'user_count': user_count,
                'user': User.objects.get(id=request.session['user_id'])
            }
            return render(request, 'welcomeadmin.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')


def request(request):
    if 'user_id' in request.session:
        if request.session['user_role'] == 3:
            return render(request, 'request.html')
        else:
            return redirect('/')
    else:
        return redirect('/')


def artistrequest(request):
    if 'user_id' in request.session:
        if request.session['user_role'] == 1:
            artist_requests = User.objects.filter(role_id=4)
            context = {
                'all': artist_requests,
                'user': User.objects.get(id=request.session['user_id'])
            }
            return render(request, 'artistrequest.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')


def artistRequest(request):
    if 'user_id' in request.session:
        if request.session['user_role'] == 3:
            user = User.objects.get(id=request.session['user_id'])
            user.role = Role.objects.get(id=4)
            user.save()
            request.session['user_role'] = 4
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')


def addmusic(request):
    return render(request, 'addmusic.html')


def addmusicevent(request):
    if 'user_id' in request.session:
        Role = Role.objects.get(id=1)
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        if user.role == Role:
            return render(request, 'addmusicevent.html')
        else:
            return redirect('/')
    else:
        return redirect('/')


def allmusic(request):
    music = Music.objects.all()
    print(music)


def event(request, id):
    event = Event.objects.get(id=id)
    soldtickets = Ticket.objects.filter(event=event).count()
    context = {
        'event': event,
        'soldtickets': soldtickets
    }
    return render(request, 'soloEvent.html', context)


def clearify():
    if Role.objects.all().count() == 0:
        Role.objects.create(name="Admin")
        Role.objects.create(name="Artist")
        Role.objects.create(name="User")
        Gender.objects.create(name="Male")
        Gender.objects.create(name="Female")
        Gender.objects.create(name="Other")
