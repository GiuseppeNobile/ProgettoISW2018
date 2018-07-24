from django.shortcuts import render
from .models import *


#def listaPrenotazioni(request):
  #  return render(request, 'listaPrenotazioni.html')


#def login(request):
 #   return render(request, 'login.html')


#def dettaglioPrenotazione(request):
 #   return render(request, 'dettaglioPrenotazione.html')


def homeAlbergatore(request):
    context ={}
    return render(request, 'homeAlbergatore.html', context)


