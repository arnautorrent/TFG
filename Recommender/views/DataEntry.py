# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.constants import Constants

def DataEntry(request):
    template_name = 'Recommender/data_entry.html'
    genre_list = {'Rock', 'Pop', 'Folk', 'Classica', 'Popular', 'Punk', 'Metal', 'Soul', 'Flamenc', 'Rumba', 'Ska',
                  'Reggae', 'Disco', 'Cantautor', 'Funk', 'Electrònica', 'Blues', 'Jazz', 'Indie', 'Country'}
    array = range(2,Constants.NUMBER_OF_FIELDS + 1)
    context = {'genre_list':genre_list,
               'array':array}
    return render(request,template_name, context)