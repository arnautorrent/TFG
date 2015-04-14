from django.db import models

class MusicGenres(models.Model):
    genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.genre



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



class Playlists(models.Model):
   user = models.ForeignKey('Users')
   s1 = models.ForeignKey('Songs', related_name = 'song1')
   s2 = models.ForeignKey('Songs', related_name = 'song2')
   s3 = models.ForeignKey('Songs', related_name = 'song3')
   s4 = models.ForeignKey('Songs', related_name = 'song4')
   s5 = models.ForeignKey('Songs', related_name = 'song5')
   s6 = models.ForeignKey('Songs', related_name = 'song6')
   s7 = models.ForeignKey('Songs', related_name = 'song7')
   s8 = models.ForeignKey('Songs', related_name = 'song8')
   s9 = models.ForeignKey('Songs', related_name = 'song9')
   s10 = models.ForeignKey('Songs', related_name = 'song10')
   s11 = models.ForeignKey('Songs', related_name = 'song11')
   s12 = models.ForeignKey('Songs', related_name = 'song12')
   s13 = models.ForeignKey('Songs', related_name = 'song13')
   s14 = models.ForeignKey('Songs', related_name = 'song14')
   s15 = models.ForeignKey('Songs', related_name = 'song15')
   s16 = models.ForeignKey('Songs', related_name = 'song16')
   s17 = models.ForeignKey('Songs', related_name = 'song17')
   s18 = models.ForeignKey('Songs', related_name = 'song18')
   s19 = models.ForeignKey('Songs', related_name = 'song19')
   s20 = models.ForeignKey('Songs', related_name = 'song20')

   def __unicode__(self):
       return self



class Forms(models.Model):
    places_lived = models.CharField(max_length = 500)
    preferred_genres = models.CharField(max_length = 500)
    preferred_artists = models.CharField(max_length = 500)
    preferred_songs = models.CharField(max_length = 500)

    def __unicode__(self):
        return self