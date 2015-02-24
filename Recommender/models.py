from django.db import models

class MusicGenre(models.Model):
    genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.genre