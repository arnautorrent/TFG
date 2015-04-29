# -*- coding: UTF-8 -*-

from django.shortcuts import render
from Recommender.models import Users, Songs, Forms

def SaveData(request):

    # TODO Filtrar les dades (sanitize)

    # [PROVES AMB LA BDD]
    # all_songs = Songs.objects.all()
    # for song in all_songs:
    #     if song.album == '':
    #         song.album = None
    #         song.save()


    # TODO Validar les dades

    # FILL DB
    #fill_db_user_table(request)
    #get last User_ID and set it in the SESSION.
    #fill_db_form_table

    # RENDER (Estem processant les teves dades...) -> Ens porta a una 3a pàgina amb la playlist feta!
    template_name = 'Recommender/save_data.html'
    context = {'firstName':request.POST.get("inputFirstName")}
    return render(request, template_name, context)


def fill_db_user_table(request):
    u = Users(first_name = request.POST.get("inputFirstName"),
              last_name = request.POST.get("inputLastName"),
              birth_place = request.POST.get("inputBirthPlace"),
              birth_date = request.POST.get("inputBirthDate"))
    u.save()


def fill_db_form_table(request):
    f = Forms(places_lived = 0,
              preferred_genres = 0,
              preferred_artists = 0,
              preferred_songs = 0,
              like_dancing = 0,
              play_instrument = 0,
              instrument = 0)
    f.save()