# -*- coding: UTF-8 -*-

from django.shortcuts import render
import time
from Recommender.models import Users, Songs
from Recommender.constants import Constants
from pyechonest import config, artist, song


def MainAlgorithm(request):
    #TODO Calcular la llista
    time.sleep(10)




    #ADAPTACIÓ ALGORITME GUILLEM

    config.ECHO_NEST_API_KEY = Constants.ECHONEST_API_KEY #Poso la API key
    playlist_length = 18
    percentage_of_direct_musical_data = 0.50

    #===============================LOAD USER INFORMATION================================
    # He de mirar l'ID, i agafar les dades que toquin de la BDD.
    # DADES:
    #   - Nom
    #   - Email ?
    #   - Data de naixement
    #   - LLoc de naixement
    #   - LLocs on ha viscut
    #   - Gèneres preferits
    #
    #


    #=======================================================









    # RENDER la playlist
    template_name = 'Recommender/results.html'
    context = {'firstName':'playlist'}
    return render(request,template_name, context)