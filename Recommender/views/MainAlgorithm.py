from django.shortcuts import render
import time
from Recommender.models import Users, Songs
from Recommender.constants import Constants

def MainAlgorithm(request):
    #TODO Calcular la llista
    time.sleep(10)

    # RENDER la playlist
    template_name = 'Recommender/results.html'
    context = {'firstName':'playlist'}
    return render(request,template_name, context)