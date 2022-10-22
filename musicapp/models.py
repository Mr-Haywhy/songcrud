from django.db import models


# Create your models here.
class Artise(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=200)


class Lyric(models.Model):
    content = models.CharField(max_length=500)
    sond_id = models.CharField(max_length=200)
