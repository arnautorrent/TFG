from django.db import models

class MusicGenre(models.Model):
    genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.genre


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=200)

    def __unicode__(self):
        return self


# class Form(models.Model):
#
#    def __unicode__(self):
#        return self


#class Song(models.Model):
#   model.CharField(max_length=200)
#
#    def __unicode__(self):
#        return self

#class Year(models.Model):
#
#
#    def __unicode__(self):
#        return self


#class Playlist(models.Model):
#    user = model.ForeignKey(User)
#    s1 = model.ForeignKey(Song)
#    s2 = model.ForeignKey(Song)
#    s3 = model.ForeignKey(Song)
#    s4 = model.ForeignKey(Song)
#    s5 = model.ForeignKey(Song)
#    s6 = model.ForeignKey(Song)
#    s7 = model.ForeignKey(Song)
#    s8 = model.ForeignKey(Song)
#    s9 = model.ForeignKey(Song)
#    s10 = model.ForeignKey(Song)
#    s11 = model.ForeignKey(Song)
#    s12 = model.ForeignKey(Song)
#    s13 = model.ForeignKey(Song)
#    s14 = model.ForeignKey(Song)
#    s15 = model.ForeignKey(Song)
#    s16 = model.ForeignKey(Song)
#    s17 = model.ForeignKey(Song)
#    s18 = model.ForeignKey(Song)
#    s19 = model.ForeignKey(Song)
#    s20 = model.ForeignKey(Song)
#
#    def __unicode__(self):
#        return self