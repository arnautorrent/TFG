# -*- coding: UTF-8 -*-

from django.shortcuts import render
import time
from Recommender.models import Users, Songs
from Recommender.constants import Constants
from pyechonest import config, artist, song


def MainAlgorithm(request):
    #TODO ADAPTACIÓ ALGORITME GUILLEM

    config.ECHO_NEST_API_KEY = Constants.ECHONEST_API_KEY #Poso la API key
    playlist_length = 20
    percentage_of_direct_musical_data = 0.50

    #===========================LOAD USER $ FORM INFORMATION=============================
    #
    # He de mirar l'ID, i agafar les dades que toquin de la BDD:
    #   - Nom
    #   - Data de naixement
    #   - LLoc de naixement
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
    # 3) Fem una llista d'artistes similars.
    # 4) Fem una llista de "TOP SONGS" dels artistes similars.
    #
    #============================PREFERENCE FILTER 1=====================================
    #
    # És la llista amb cançons preferides i cançons TOP dels artistes preferits
    # i relacionats fins a arribar al percentage_of_direct_musical_data.
    #
    #============================PREFERENCE FILTER 2=====================================
    #
    # Aquí farem cerques de possibles cançons per regió/localització, tempo, ballable,
    # estil, any, ... [[AQUÍ ÉS ON HI HA LA XIXA DE MILLORA DE L'ALGORITME]].
    #
    #====================================================================================

    # RENDER la playlist
    template_name = 'Recommender/results.html'
    context = {'playlist':'playlist'}
    return render(request,template_name, context)