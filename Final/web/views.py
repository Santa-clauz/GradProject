from django.http import HttpResponse
from web.models import *
from django.shortcuts import render, redirect
import bcrypt

def landing_page(request):
    return render(request, 'landing_page.html')

def category(request):
    return render(request, 'category.html')

def blog(request):
    return render(request, 'blog.html')

def artist(request):
    return render(request, 'artist.html')

def playlist(request):
    return render(request, 'playlist.html')


def About(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact.html')


def Login(request):
    return render(request, 'Login.html')


def registration(request):
    return render(request, 'registration.html')

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

