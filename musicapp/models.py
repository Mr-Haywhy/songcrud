from unicodedata import name
from django.db import models


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name}({self.last_name})({self.age})"


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __init__(self, title, date_released, likes, artiste_id):
        self.title = title
        self.date_released = date_released
        self.likes = likes
        self.artiste_id = artiste_id

    def __str__(self):
        return f"{self.title}({self.date_released})({self.likes})({self.artiste_id})"


class Lyric(models.Model):
    content = models.CharField(max_length=500)
    song_id = models.ForeignKey(Song, on_delete=models.DO_NOTHING)

    def __init__(self, content, song_id):
        self.content = content
        self.song_id = song_id

    def __str__(self):
        return f"{self.content}({self.song_id})"
