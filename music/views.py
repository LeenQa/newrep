from django.shortcuts import render, get_object_or_404
from django.shortcuts import  render
from music.models import Album,Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class UserFormView(View):
    form_class= UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.changed_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()


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
    except (KeyError,Song.DoesNotExist):
        return render(request, "music/detail.html", {'album': album, 'error_message': 'you did not select a valid song',})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,"music/detail.html", {'album': album})


