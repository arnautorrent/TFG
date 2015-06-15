# -*- coding: UTF-8 -*-

import os
from mutagen.mp3 import MP3
from Recommender.models import Songs
import requests

def Proves(request):
    #Extreure_tags_ID3(request)
    #Extreure_tags_AcousticBrainz(request)
    print 'Accessible només usuaris autoritzats'

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
    for root, dirs, files in os.walk("/Users/arnau/Desktop/music_new", topdown=True):
        for name in files:
            fileName, fileExtension = os.path.splitext(name)
            if fileExtension == '.mp3':
                path = root + '/' + fileName + fileExtension
                tags = MP3(path)
                try:
                    title = tags['TIT2'][0]
                    try:
                        song = Songs.objects.get(title = title)
                    except:
                        try:
                            artist = tags['TPE1'][0]
                        except:
                            artist = "unknown"
                        try:
                            album = tags['TALB'][0]
                        except:
                            album = None
                        try:
                            date = tags['TDRC'][0].year
                        except:
                            date = None
                        tempo = None
                        try:
                            mbid = tags['UFID:http://musicbrainz.org'].data
                        except :
                            mbid = None
                        s = Songs(title = title, artist = artist, album = album, year = date, tempo = tempo, mbid = mbid)
                        s.save()
                except:
                    print path