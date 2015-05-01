# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import Users, Forms
from Recommender.constants import Constants

def SaveData(request):
    #Creo una variable amb els llocs on ha viscut i els anys
    livedPlaces = ''
    for x in range(1,Constants.NUMBER_OF_FIELDS + 1):
        aux1 = "inputLivedPlace" + str(x)
        aux2 = "inputStartYear" + str(x)
        aux3 = "inputEndYear" + str(x)
        if (request.POST.get(aux1)):
            livedPlaces = livedPlaces + request.POST.get(aux1) + '(' + request.POST.get(aux2) + '-' + request.POST.get(aux3) + ')' + '//'
        else:
            livedPlaces = livedPlaces[:-2]
            break


    #Creo una variable amb els estils preferits
    preferredGenres = ''
    for x in range(1,Constants.NUMBER_OF_GENRES + 1):
        aux1 = "inputFavouriteFlavour" + str(x)
        if (request.POST.get(aux1)):
            preferredGenres = preferredGenres + request.POST.get(aux1) + '//'
    if (preferredGenres):
        preferredGenres = preferredGenres[:-2]


    #Creo una variable amb els artistes preferits
    preferredArtists =''
    for x in range(1,Constants.NUMBER_OF_GENRES + 1):
        aux1 = "inputFavouriteArtist" + str(x)
        if (request.POST.get(aux1)):
            preferredArtists = preferredArtists + request.POST.get(aux1) + '//'
        else:
            preferredArtists = preferredArtists[:-2]
            break


    #Creo una variable amb les cançons preferides i l'artista
    preferredSongs =''
    for x in range(1,Constants.NUMBER_OF_GENRES + 1):
        aux1 = "inputFavouriteSong" + str(x)
        aux2 = "inputArtistSong" + str(x)
        if (request.POST.get(aux1)):
            if (request.POST.get(aux2)):
                preferredSongs = preferredSongs + request.POST.get(aux1) + '(' + request.POST.get(aux2) + ')' + '//'
            else:
                preferredSongs = preferredSongs + request.POST.get(aux1) + '//'
        else:
            preferredSongs = preferredSongs[:-2]
            break


    #Creo una variable amb el nom de l'instrument que sap tocar (o NULL si no en sap tocar cap)
    if (request.POST.get("inputInstrument")):
        instrumentName = request.POST.get("inputInstrumentName")
    else:
        instrumentName = None


    # TODO Filtrar les dades (sanitize)
    # TODO Validar les dades


    #Omplo la BDD
    fill_db(request, livedPlaces, preferredGenres, preferredArtists, preferredSongs, instrumentName)
    template_name = 'Recommender/save_data.html'
    wait = ((Constants.WAITING_TIME - 1) * 1000) / 100
    context = {'firstName':request.POST.get("inputFirstName"),
               'wait':wait}
    return render(request, template_name, context)


def fill_db(request, livedPlaces, preferredGenres, preferredArtists, preferredSongs, instrument):
    u = Users(first_name = request.POST.get("inputFirstName"),
              last_name = request.POST.get("inputLastName"),
              birth_place = request.POST.get("inputBirthPlace"),
              birth_date = request.POST.get("inputBirthDate"))
    u.save()
    request.session['user_id'] = u.id

    f = Forms(places_lived = livedPlaces,
              preferred_genres = preferredGenres,
              preferred_artists = preferredArtists,
              preferred_songs = preferredSongs,
              like_dancing = request.POST.get("inputDancing"),
              play_instrument = request.POST.get("inputInstrument"),
              instrument = instrument)
    f.save()
    request.session['form_id'] = f.id