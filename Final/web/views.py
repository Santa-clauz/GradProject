from web.models import *
from django.shortcuts import render, redirect
import bcrypt
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
from time import strftime



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

def request(request):
    return render(request, 'request.html')


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

def login(request):
    print("login l7al222")
    return render(request,'login.html')

def Login(request):
    print("login l7al")
    return render(request, 'Login.html')

# def loginP(request):
#     print("helloooooooooooooooooooooooooooooo")
#     redirect('/LoginT')
#     email = request.POST['Email']
#     password = request.POST['password']
#     print(email,password)
#     errors = models.login_user(email , password)
    
#     if len(errors)>0:
#         for key,value in errors.items():
#             messages.error(request,value)
#         return redirect('/LoginT')

#     user = models.get_this_user_by_email(request.POST['email'])
#     if 'LoginT' not in request.session: #if user already logged in before
#         request.session['Name'] = user[0].username
#         request.session['email'] = user[0].email
#         request.session['phone']=user[0].phone
#         request.session['id'] = user[0].id
#         print(request.session['Name'])
#         return redirect('/home')
#     else:
#         return redirect('/LoginT')

def loginP(req):
    redirect('/login')
    req.session.clear()
    user = User.objects.filter(username=req.POST['Email'])
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
    clearify()
    gender_id = req.POST['gender']
    user_gender = Gender.objects.get(id = gender_id)
    x = req.FILES.get('upload')
    print(x)
    testzz = req.FILES['upload']
    user = User.objects.create(
        username=req.POST['username'],
        email=req.POST['email'],
        password=bcrypt.hashpw(req.POST['password'].encode(), bcrypt.gensalt()).decode(),
        birthdate=req.POST['birthdate'],
        phone=req.POST['phone'],
        address=req.POST['address'],
       
        role=Role.objects.get(id=3),
      
        gender = user_gender,
        image = x
    )
    return redirect('/')

def test(req):
    return render(req, 'test.html')

def About(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact.html')





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
        Role = Role.objects.get(id=1)
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        if user.role == Role:
            return render(request, 'welcomeadmin.html')
        else:
            return redirect('/')
    else:
        return redirect('/')


def clearify():
    if Role.objects.all().count() == 0:
        Role.objects.create(name="Admin")
        Role.objects.create(name="Artist")
        Role.objects.create(name="User")
        Gender.objects.create(name="Male")
        Gender.objects.create(name="Female")
        Gender.objects.create(name="Other")