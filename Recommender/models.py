# -*- coding: UTF-8 -*-

from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)



class Songs(models.Model):
  title = models.CharField(max_length = 200)
  artist = models.CharField(max_length = 200)
  album = models.CharField(max_length = 200)
  year = models.IntegerField(null = 'true')
  tempo = models.IntegerField(default = 100, null = 'true')
  location = models.CharField(max_length = 200)



class Forms(models.Model):
    places_lived = models.CharField(max_length = 500)
    preferred_genres = models.CharField(max_length = 500)
    preferred_artists = models.CharField(max_length = 500)
    preferred_songs = models.CharField(max_length = 500)
    like_dancing = models.BooleanField(default = 'true')
    play_instrument = models.BooleanField(default = 'true')
    instrument = models.CharField(max_length = 200, null = 'true')

    def __unicode__(self):
        return self