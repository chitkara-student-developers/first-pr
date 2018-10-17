from django.db import models

class Album(models.Model):
    artist=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    songs=models.CharField(max_length=250)
    Album_title=models.CharField(max_length=250)
    Album_logo=models.CharField(max_length=1000)

    def __str__(self):
       return self.Album_title+'-'+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    Song_title=models.CharField(max_length=250)

    def __str__(self):
        return self.Song_title