from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='home'),
    path('category', views.category, name='category'),
    path('blog', views.blog, name='blog'),
    path('artist', views.artist, name='artist'),
    path('playlist', views.playlist, name='playlist'),
    path('contact', views.contact, name='contact'),
    path('About', views.About, name='About'),
    path('test', views.test, name='index'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    # path('logout', views.logout, name='logout'),
    # path('profile/<int:id>', views.profile, name='profile'),
    # path('profile/<int:id>/edit', views.edit, name='edit'),
    # path('song/<int:id>', views.song, name='song'),
    # path('addsong', views.addsong, name='addsong'),
    # path('requestToBeArtist', views.requestToBeArtist, name='requestToBeArtist'),
    # path('admin', views.admin, name='admin'),
    # path('admin/acceptArtist/<int:id>', views.acceptArtist, name='acceptArtist'),
    # path('admin/declineArtist/<int:id>', views.declineArtist, name='declineArtist'),
    # path('admin/allArtists', views.allArtists, name='allArtists'),
    # path('admin/allUsers', views.allUsers, name='allUsers'),
    # path('admin/allSongs', views.allSongs, name='allSongs'),
    # path('admin/allAlbums', views.allAlbums, name='allAlbums'),
    # path('admin/allPlaylists', views.allPlaylists, name='allPlaylists'),

]

