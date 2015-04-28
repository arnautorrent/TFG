# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import Users, Songs
from Recommender.constants import Constants
from pyechonest import config, artist, song


def MainAlgorithm(request):
    #TODO ADAPTACIÓ ALGORITME GUILLEM
    config.ECHO_NEST_API_KEY = Constants.ECHONEST_API_KEY #Poso la API key
    request.session['user_id'] = 13
    playlist_length = 20
    percentage_of_direct_musical_data = 0.50

    #===========================LOAD USER & FORM INFORMATION=============================
    #
    # He de mirar l'ID, i agafar les dades que toquin de la BDD:
    user = {}
    user['id'] = request.session['user_id']
    user['name'] = Users.objects.get(id = request.session['user_id']).first_name
    user['birth_date'] = Users.objects.get(id = request.session['user_id']).birth_date
    user['birth_place'] = Users.objects.get(id = request.session['user_id']).birth_place
    #   - LLocs on ha viscut
    #   - Gèneres preferits
    #   - Cançons preferides
    #   - Artistes preferits
    #
    # LA PLAYLIST ÉS UN VECTOR AMB ID'S DE CANÇONS DE LA BDD???
    #
    #==============================FAVOURITE SONGS=======================================
    #
    # 1) Fem una llista amb les cançons preferides (aquestes hi van segur).
    #
    #==================================ARTISTS===========================================
    #
    # 1) Fem una llista amb els artistes preferits.
    # 2) Afegim els artistes de les cançons preferides.
    # 3) Anem afegint les TOP SONGS de cada un d'aquests artistes fins a arribar al
    #    límit marcat per percentage_of_direct_musical_data
    #
    #============================PREFERENCE FILTER 1=====================================
    #
    # Fins ara era agafar artistes similars i fer la TOP SONG.
    #
    # Aquí és on s'hauria de millorar. Podem fer cerques per tempo, ballable,
    # estil, instruments, llengua, temàtica, ... (incorporar dades a la BDD).
    #
    #============================PREFERENCE FILTER 2=====================================
    #
    # Aquí selecciona dues cançons: una de la zona geogràfica i època. Cançons entre
    # els 0 i 30 anys de vida (anys de rellevància). Mirem a quin país vivia durant
    # aquestes edats. Que torni una cançó del gènere folk, i una del genere preferit
    # de l'usuari o sense especificar gènere (tornarà una cançó popular de l'època).
    #
    #====================================================================================


    # RENDER la playlist†
    template_name = 'Recommender/results.html'
    context = {'playlist':'playlist'}
    return render(request,template_name, context)