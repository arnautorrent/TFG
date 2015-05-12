# -*- coding: UTF-8 -*-

import os
from mutagen.mp3 import MP3
from Recommender.models import Songs

def Proves(request):


    count = 0
    for root, dirs, files in os.walk("/Users/arnau/Desktop/music", topdown=True):
        for name in files:
            fileName, fileExtension = os.path.splitext(name)
            if fileExtension == '.mp3':
                count += 1
                song = Songs.objects.get(id = count)
                path = root + '/' + fileName + fileExtension
                tags = MP3(path)
                try :
                    mbid = tags['TXXX:MusicBrainz Release Track Id'][0]
                    song.mbid = mbid
                    song.save()
                except :
                    song.mbid = None
                    song.save()
