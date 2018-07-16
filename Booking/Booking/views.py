from django.shortcuts import render


def listaPrenotazioni(request):
    return render(request, 'templates/listaPrenotazioni.html', {})


def login(request):
    return render(request, 'templates/login.html', {})


def dettaglioPrenotazione(request):
    return render(request, 'templates/prenotazioneDettaglio.html', {})