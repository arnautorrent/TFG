# -*- coding: UTF-8 -*-

import os
from mutagen.mp3 import MP3
from Recommender.models import Songs
import requests

def Proves(request):
    print "Accessible només a usuaris autoritzats o Administradors"


def Extreure_tags_AcousticBrainz(request):
    url_base = 'http://acousticbrainz.org/'
    low_level = '/low-level'
    all_songs = Songs.objects.all()
    for song in all_songs:
        try:
            MBID = song.mbid.encode()
            r = requests.get(url_base + MBID + low_level)
            j = r.json()
            song.tempo = int(j['rhythm']['bpm'])
            song.genre = j['metadata']['tags']['genre'][0]
            song.danceability = j['rhythm']['danceability']
            song.save()
        except:
            pass


def Extreure_tags_ID3(request):
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
                    mbid = tags['UFID:http://musicbrainz.org'].data
                    song.mbid = mbid
                    song.save()
                except :
                    song.mbid = None
                    song.save()
