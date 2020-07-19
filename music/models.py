from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo=models.FileField()

    def __str__(self):
        return f"{self.album_title}, {self.artist}"

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{str(self.album)}, {self.song_title}"
