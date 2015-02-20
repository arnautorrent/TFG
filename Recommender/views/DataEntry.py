from django.shortcuts import render

def DataEntry(request):
    template_name = 'Recommender/data_entry.html'
    return render(request,template_name)