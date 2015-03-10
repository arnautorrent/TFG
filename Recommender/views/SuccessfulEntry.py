from django.shortcuts import render
from Recommender.models import User

def SuccessfulEntry(request):

    # SANITIZE

    # VALIDATE

    # FILL DB
    u = User(first_name = request.POST.get("inputFirstName"),
             last_name = request.POST.get("inputLastName"),
             birth_place = request.POST.get("inputBirthPlace"),
             birth_date = request.POST.get("inputBirthDate")
    )
    u.save()

    # f = Form()
    # f.save()

    #RENDER (Estem processant les teves dades...) -> Ens porta a una 3a pagina amb la playlist feta!
    template_name = 'Recommender/successful_entry.html'
    context = {'method':request.POST.get("inputFirstName")}
    return render(request, template_name, context)

def fill_db():
    u = User(first_name = request.POST.get("inputFirstName"),
             last_name = request.POST.get("inputLastName"),
             birth_place = request.POST.get("inputBirthPlace"),
             birth_date = request.POST.get("inputBirthDate")
    )
    u.save()