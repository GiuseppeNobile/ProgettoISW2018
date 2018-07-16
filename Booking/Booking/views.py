from django.shortcuts import render


def listaPrenotazioni(request):
    return render(request, 'listaPrenotazioni.html')


def login(request):
    return render(request, 'login.html')


def dettaglioPrenotazione(request):
    return render(request, 'dettaglioPrenotazione.html')


def home(request):
    return render(request, 'home.html')