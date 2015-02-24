from django.shortcuts import render
from Recommender.models import MusicGenre

def DataEntry(request):
    template_name = 'Recommender/data_entry.html'
    genre_list = MusicGenre.objects.all()
    context = {'genre_list':genre_list }
    return render(request,template_name, context)