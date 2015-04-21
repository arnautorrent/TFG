# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import Users, Songs

def SuccessfulEntry(request):

    # TODO Filtrar les dades (sanitize)

    # [PROVES AMB LA BDD]
    all_songs = Songs.objects.all()
    for song in all_songs:
        if song.album == '':
            song.album = None
            song.save()


    # TODO Validar les dades

    # FILL DB
    #fill_db(request)

    # RENDER (Estem processant les teves dades...) -> Ens porta a una 3a pàgina amb la playlist feta!
    template_name = 'Recommender/successful_entry.html'
    context = {'firstName':request.POST.get("inputFirstName")}
    return render(request, template_name, context)


def fill_db(request):
    u = Users(first_name = request.POST.get("inputFirstName"),
             last_name = request.POST.get("inputLastName"),
             birth_place = request.POST.get("inputBirthPlace"),
             birth_date = request.POST.get("inputBirthDate")
    )
    u.save()