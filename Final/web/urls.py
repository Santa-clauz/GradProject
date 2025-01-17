from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('Artists', views.artists, name='artists'),
    path('blog', views.blog, name='blog'),
    #path('artist/<int:id>', views.artist, name='artist'),
    path('music/<int:id>', views.music, name='music'),
    #path('artists', views.artists, name='artists'),
    path('artist/<int:id>', views.artist, name='artist'),
    path('contact', views.contact, name='contact'),
    path('About', views.About, name='About'),
    path('LoginT', views.Login, name='index'),
    path('LoginP', views.loginP, name='loginP'),
    path('registration', views.registration, name='registration'),
    path('register', views.register, name='register'),
    path('create_event', views.create_Event,name='create_event'),
    path('artist_request', views.request,name='request'),
    path('admin/', views.admin_login),
    path('addmusic', views.addmusic),
    path('addmusicevent', views.addmusicevent),
    path('allmusic', views.allmusic),
    path('logout', views.logout),
    path('artistrequest', views.artistrequest),
    path('artistRequest', views.artistRequest),
    path('acceptartist/<int:id>', views.acceptartist),
    path('declineartist/<int:id>', views.declineartist),
    path('adminallusers', views.adminallusers),
    path('adminallmusic', views.adminallmusic),
    path('adminallevents', views.adminallevents),
    path('adminallartists', views.adminallartists),
    path('create_song', views.create_song),
    path('musicadd', views.musicadd),
    path('eventadd', views.eventadd),
    path('Events', views.Events, name='Events'),
    path('event/<int:id>', views.event, name='event'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('searchArtist', views.searchArtist, name='searchArtist'),
    path('searchEvent', views.searchEvent, name='searchEvent'),
    path('like/<int:id>', views.like, name='like'),
    path('dislike/<int:id>', views.dislike, name='dislike'),
    # path('adminProfile', views.adminprofile),
    # path('adminhandle', views.adminhandle),
    # path('artistrequest', views.artistrequest),
    # path('acceptartist/<int:id>', views.acceptartist),
    # path('declineartist/<int:id>', views.declineartist),
    # path('adminallusers', views.allusers),
    # path('allmusic', views.allmusic),
    # path('deleteuser/<int:id>', views.deleteuser),
    # path('deletemusic/<int:id>', views.deletemusic),
    # path('update/<int:id>', views.update),
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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)