from django.shortcuts import render
from .models import *



def hotels(request):
    alberghi = Hotel.objects.all().order_by('nomehotel')
    return render(request, 'hotels.html', {'alberghi': alberghi})


def homeAlbergatore(request):
    prenotazioni = Prenotazione.objects.all().order_by('data')
    return render(request, 'homeAlbergatore.html', {'prenotazioni': prenotazioni})

def search(request):
    context={}
    return render(request, 'search.html', {})

