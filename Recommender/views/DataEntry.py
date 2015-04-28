# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import MusicGenres

def DataEntry(request):
    template_name = 'Recommender/data_entry.html'
    #genre_list = MusicGenres.objects.all()
    genre_list = {'Rock', 'Pop', 'Folk', 'Classica', 'Popular', 'Punk', 'Metal', 'Soul', 'Flamenc', 'Rumba', 'Ska',
                  'Reggae', 'Disco', 'Cantautor', 'Funk', 'Electrònica', 'Blues', 'Jazz', 'Indie', 'Country'}
    array2to10 = range(2,11)
    context = {'genre_list':genre_list,
               'array2to10':array2to10}
    return render(request,template_name, context)