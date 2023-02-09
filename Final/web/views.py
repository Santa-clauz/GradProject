from django.http import HttpResponse
from web.models import *
from django.shortcuts import render, redirect
import bcrypt
from django.core.paginator import Paginator


def landing_page(request):
    return render(request, 'landing_page.html')

def category(request):
    return render(request, 'category.html')

def blog(request):
    return render(request, 'blog.html')


def create_music(request):
    return render(request, 'create_music.html')

def create_playlist(request):
    return render(request, 'create_playlist.html')


def create_Event(request):
    return render(request, 'create_event.html')


def artist(request):
    artist = User.objects.get(id=id)
    context = {
        'artist': artist,
    }
    return render(request,context, 'artist.html')

def artist(request):
    # artist = User.objects.get(id=id)
    # context = {
    #     'artist': artist,
    # }
    return render(request, 'artist.html')

def playlist(request):
    # playlist = Playlist.objects.get(id=id)
    # context = {
    #     'playlist': playlist,
    # }
    return render(request, 'playlist.html')

def artists(request):
    # artistRole = Role.objects.get(id=2)
    # artists = User.objects.all(Role=artistRole)
    # context = {
    #     'artists': artists,
    # }
    return render(request, 'artists.html')

def playlists(request):
    # playlists = Playlist.objects.all()
    # context = {
    #     'playlists': playlists,
    # }
    # paginator = Paginator(playlists, 5)
    # page = request.GET.get('page')
    # posts = paginator.get_page(page)

    # {'posts': posts}
    return render(request, 'playlists.html',)


def music(request):
    music = Music.objects.get(id=id)
    context = {
        'music': music,
    }
    return render(request, 'music.html')

def login(req):
    redirect('/login')
    req.session.clear()
    user = User.objects.filter(username=req.POST['username'])
    password=req.POST['password']
    if user:
        logged_user = user[0].id
        if bcrypt.checkpw(password.encode() , logged_user.password.encode()):
            req.session['user_id'] = logged_user.id
            return redirect('/')
        else:
            req.session['wrong_password'] = "Please Check Password"
            return redirect('/login')
    else:
        req.session['wrong_username'] = "Please Check Username"
        return redirect('/login')

def register(req):
    redirect('/register')
    if 'user_id' in req.session:
        return redirect('/')
    user = User.objects.create(
        username=req.POST['username'],
        password=bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt()).decode(),
        email=req.POST['email'],
        first_name=req.POST['first_name'],
        
    )

def test(req):
    return render(req, 'test.html')

def About(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact.html')


def Login(request):
    return render(request, 'Login.html')


def registration(request):
    return render(request, 'registration.html')



def admin_login(request):
    if 'user_id' in request.session:
        Role = Role.objects.get(id=1)
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        if user.role == Role:
            return render(request, 'welcomeadmin.html')
        else:
            return redirect('/')
    else:
        return redirect('/')

 