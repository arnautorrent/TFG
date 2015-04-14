from django.shortcuts import render
from Recommender.models import Users, Songs

def SuccessfulEntry(request):

    # SANITIZE

    #[PROVES AMB LA BDD]
    all_songs = Songs.objects.all()
    for song in all_songs:
        if song.album == '':
            song.album = None
            song.save()





    # VALIDATE

    # FILL DB
    #fill_db(request)

    #RENDER (Estem processant les teves dades...) -> Ens porta a una 3a pagina amb la playlist feta!
    template_name = 'Recommender/successful_entry.html'
    context = {'method':request.POST.get("inputFirstName")}
    return render(request, template_name, context)

def fill_db(request):
    u = Users(first_name = request.POST.get("inputFirstName"),
             last_name = request.POST.get("inputLastName"),
             birth_place = request.POST.get("inputBirthPlace"),
             birth_date = request.POST.get("inputBirthDate")
    )
    u.save()