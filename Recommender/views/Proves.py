# -*- coding: UTF-8 -*-

import os
from mutagen.mp3 import MP3
from Recommender.models import Songs
from django.shortcuts import render
from Recommender.models import Users, Forms, Songs
from Recommender.constants import Constants
from pyechonest import config, artist, song
import musicbrainzngs
import requests

def Proves(request):
    #musicbrainzngs.set_useragent('life_soundtrack','0.1')
    #musicbrainzngs.set_rate_limit('false')
    #config.ECHO_NEST_API_KEY = Constants.ECHONEST_API_KEY #Poso la API key
    #result = musicbrainzngs.search_artists(artist= 'Vetusta Morla')
    #asdf = result['artist-list'][0]['id']
    #result2 = musicbrainzngs.browse_recordings(artist = asdf)

    # count = 0
    # for root, dirs, files in os.walk("/Users/arnau/Desktop/music", topdown=True):
    #     for name in files:
    #         fileName, fileExtension = os.path.splitext(name)
    #         if fileExtension == '.mp3':
    #             count += 1
    #             song = Songs.objects.get(id = count)
    #             path = root + '/' + fileName + fileExtension
    #             tags = MP3(path)
    #             try :
    #                 mbid = tags['UFID:http://musicbrainz.org'].data
    #                 song.mbid = mbid
    #                 song.save()
    #             except :
    #                 song.mbid = None
    #                 song.save()




    url_base = 'http://acousticbrainz.org/'
    high_level = '/high-level'
    low_level = '/low-level'
    asdf = 2
    all_songs = Songs.objects.all()
    for song in all_songs:
        try:
            MBID = song.mbid.encode()
            r = requests.get(url_base + MBID + low_level)
            j = r.json()
            asdf = 2
            song.tempo = int(j['rhythm']['bpm'])
            song.genre = j['metadata']['tags']['genre'][0]
            song.danceability = j['rhythm']['danceability']
            song.save()
            print song.id
        except:
            pass


def Proves_velles(request):
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
