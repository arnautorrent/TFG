# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import Users, Forms, Songs
from Recommender.constants import Constants
from pyechonest import config, artist, song
from random import randint
from geopy.geocoders import Nominatim
import time
import re
import operator
import musicbrainzngs




def MainAlgorithm(request):
    musicbrainzngs.set_useragent('life_soundtrack','0.1')
    musicbrainzngs.set_rate_limit('false')
    config.ECHO_NEST_API_KEY = Constants.ECHONEST_API_KEY #Poso la API key
    config.CALL_TIMEOUT = 100
    playlist = []

    #LOAD USER INFORMATION:
    user = load_user_information(request)
    #DIRECT SONGS:
    direct_songs(user,playlist)

    if len(playlist) < (Constants.PLAYLIST_LENGTH * Constants.PERCENTAGE_OF_DIRECT_MUSICAL_DATA):
        #ARTIST SONGS:
        artist_songs(user,playlist)
    if Constants.PLAYLIST_LENGTH - len(playlist) > 2:
        #SIMILARITY SONGS:
        #max_songs = Constants.PLAYLIST_LENGTH - len(playlist) - 2
        #similarity_songs(user,playlist,max_songs)
        #INDIRECT SONGS:
        indirect_songs(user,playlist)
    elif 0 < Constants.PLAYLIST_LENGTH - len(playlist) <= 2:
        #SIMILARITY SONGS:
        max_songs = Constants.PLAYLIST_LENGTH - len(playlist)
        similarity_songs(user,playlist,max_songs)

    #WAIT A BIT:
    time.sleep(Constants.WAITING_TIME)

    #RENDER RESULTS:
    template_name = 'Recommender/results.html'
    context = {'playlist' : playlist}
    return render(request,template_name, context)



#================================================================================================#
#                                       MÈTODES PER UTILITZAR:                                   #
#================================================================================================#
def load_user_information(request):
    user = {}
    #ID:
    user['id'] = request.session['user_id']
    #Nom:
    user['name'] = Users.objects.get(id = user['id']).first_name
    #Any de naixement:
    user['birth_year'] = Users.objects.get(id = user['id']).birth_date.year
    #LLoc de naixement:
    user['birth_place'] = Users.objects.get(id = user['id']).birth_place
    #LLocs on ha viscut:
    user['lived_places'] = []
    aux_lived_places = Forms.objects.get(id = user['id']).places_lived.split('//')
    for place in aux_lived_places:
        aux_city = re.search('^[A-Za-z]*', place)
        city = aux_city.group(0)
        years = re.findall('[0-9]{4}', place)
        pair_place_period = {"City" : city, "Start" : years[0], "End" : years[1]}
        user['lived_places'].append(pair_place_period)
    #Gèneres preferits:
    user['genres'] = Forms.objects.get(id = user['id']).preferred_genres.split('//')
    #Li agrada ballar?:
    user['dancing'] = Forms.objects.get(id = user['id']).like_dancing
    #Toca algun instrument?:
    if Forms.objects.get(id = user['id']).play_instrument:
        user['instrument'] = Forms.objects.get(id = user['id']).instrument
    else:
        user['instrument'] = None
    #Cançons preferides:
    user['songs'] = []
    aux_songs = Forms.objects.get(id = user['id']).preferred_songs.split('//')
    for aux_song in aux_songs:
        artist_regex = re.search('\([A-Za-z0-9\s\.\-,_]*\)$', aux_song)
        try :
            aux_artist = artist_regex.group(0)[1:-1]
        except :
            aux_artist = None
        title = re.sub('\([A-Za-z0-9\s\.\-,_]*\)$', '', aux_song)
        pair_song_artist = {"Title" : title, "Artist" : aux_artist}
        user['songs'].append(pair_song_artist)
    #Artistes preferits:
    user['artists'] = Forms.objects.get(id = user['id']).preferred_artists.split('//')
    #Artistes de les cançons preferides:
    for aux_song in user['songs']:
        if aux_song['Artist']:
            user['artists'].append(aux_song['Artist'])
    return user



def direct_songs(user,playlist):
    max_songs = Constants.PLAYLIST_LENGTH
    if len(user['songs']) <= Constants.PLAYLIST_LENGTH:
        for aux_song in user['songs']:
            new_song = Songs.objects.filter(title = aux_song['Title'])
            if new_song:
                if len(new_song) == 1:
                    #La tinc a la BDD i és única:
                    new_song = new_song[0]
                    add_to_playlist(new_song,playlist)
                else:
                    #La tinc a la BDD però no és única:
                    new_song = new_song[0] #TODO Filtrar amb preferències
                    add_to_playlist(new_song,playlist)
            else:
                #No la tinc a la BDD per tant la busco a Echonest:
                new_song = song.search(title = aux_song['Title'])
                new_song.sort(key = operator.attrgetter('song_hotttnesss'), reverse = True) #TODO Filtrar amb preferències
                new_song = new_song[0]
                add_to_playlist(new_song,playlist)
    else:
        #En principi no hi entra mai. Voldria dir que l'usuari ens ha entrat més de 20 títols de cançons directament.
        playlist = preference_filter(user['songs'],user,max_songs)



def artist_songs(user,playlist):
    max_songs = Constants.PLAYLIST_LENGTH * Constants.PERCENTAGE_OF_DIRECT_MUSICAL_DATA
    list2 = []
    for aux_artist in user['artists']:
        song_list = Songs.objects.filter(artist = aux_artist)
        if song_list:
            if len(song_list) < 5:
                list2.append(song_list)
            else:
                #5 primeres
                list2.append(song_list[0:5]) #TODO Es podria agafar la més rellevant i no una a l'atzar
        else:
            #No el tinc a la BDD, agafo la cançó TOP d'Echonest:
            while True:
                try:
                    a = artist.search(name = aux_artist)
                    a = a[0]
                    song_list = a.songs
                    if len(song_list) < 5:
                        list2.append(song_list)
                    else:
                        song_list.sort(key = operator.attrgetter('song_hotttnesss'), reverse = True)
                        list2.append(song_list[0:5])
                    break
                except:
                    time.sleep(2)
    count = 0
    while len(playlist) < max_songs:
        for s in list2:
            if len(playlist) == max_songs:
                break
            try:
                add_to_playlist(s[count],playlist)
            except:
                pass
        count += 1



def similarity_songs(user,playlist,max_songs):
    #TODO: La selecció de cançons similars
    #Agafem d'Echonest / MusicBrainz Artistes similars i Cançons similars.
    #En fem una llista i la filtrem
    #preference_filter(list,user,max_songs)
    x = 'Hello World'



def indirect_songs(user,playlist):
    max_songs = 2
    year_at_30 = user['birth_year'] + 30
    for p in user['lived_places']:
        if (int(p['Start']) <= year_at_30) and (year_at_30 < int(p['End'])):
            place_at_30 = p['City']
    geolocator = Nominatim()
    loc = geolocator.geocode(place_at_30)
    max_lat = loc.latitude + 1
    min_lat = loc.latitude - 1
    max_lon = loc.longitude + 1
    min_lon = loc.longitude - 1
    #Primer un tema Folk
    while True:
        try:
            song1 = song.search(style="folk", min_latitude = min_lat, max_latitude = max_lat, min_longitude = min_lon,
                        max_longitude = max_lon, rank_type = "familiarity", results = 20, artist_start_year_before = year_at_30)
            song1 = song1[0] #TODO Filtrar amb preferències
            add_to_playlist(song1,playlist)
            break
        except:
            pass
    #Segon un TOP HIT:
    while True:
        try:
            song2 = song.search(min_latitude = min_lat, max_latitude = max_lat, min_longitude = min_lon,
                        max_longitude = max_lon, rank_type = "familiarity", results = 20, artist_start_year_before = year_at_30)
            song2 = song2[0] #TODO Filtrar amb preferències
            add_to_playlist(song2,playlist)
            break
        except:
            pass



def preference_filter(song_list,user,max_songs):
    #TODO: El filtre de preferència
    # Ordenem amb algun sistema de puntuació (mateix instrument, mateixa llengua, mateix gènere)
    # i agafem les primeres.
    x = 'Hello World'



def add_to_playlist(song,playlist):
    if not any(s['Title'] == song.title for s in playlist):
        new_song = {}
        new_song['Title'] = song.title
        try:
            new_song['Artist'] = song.artist #Nomenclatura Base de Dades
        except:
            new_song['Artist'] = song.artist_name #Nomenclatura Echonest
        print new_song['Title']
        playlist.append(new_song)
    else:
        return
