from django.db import models


class Utente(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Albergatore(Utente):
    numeroHotel = models.IntegerField()

    def aggiungiHotel(self):
        pass


class Cliente(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def effettuaPrenotazione(self):
        pass


class Hotel(models.Model):
    nome = models.CharField(max_length=30)
    numStanze = models.IntegerField()
    proprietario = Albergatore()


class Stanza(models.Model):
    numStanza = models.IntegerField()
    hotelDiAppartenenza = Hotel()


class Prenotazione(models.Model):
    idPrenotazione = models.IntegerField()
    cliente = Cliente()
    stanza = Stanza()
    data = models.DateTimeField()