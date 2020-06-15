from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import  render
from music.models import Album,Song
from django.http import Http404

# Create your views here.

def index(request):
    album_list = Album.objects.all()
    return render(request, "music/index.html",{'album_list':album_list, })

def detail(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    return render(request,"music/detail.html", {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song= album.song_set.get(pk=request.POST['song'])
        print(request.POST['song'])
        print(selected_song)
    except (KeyError,Song.DoesNotExist):
        return render(request, "music/detail.html", {'album': album, 'error_message': 'you did not select a valid song',})
    else:
        print("got here")
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,"music/detail.html", {'album': album})