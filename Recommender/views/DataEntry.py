# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import MusicGenres

def DataEntry(request):
    template_name = 'Recommender/data_entry.html'
    genre_list = MusicGenres.objects.all()
    context = {'genre_list':genre_list }
    return render(request,template_name, context)