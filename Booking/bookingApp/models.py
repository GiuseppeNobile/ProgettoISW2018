from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Albergatore(AbstractBaseUser):
    username = models.CharField(max_length=30)
    numeroHotel = models.IntegerField()

    USERNAME_FIELD = 'username'

    def aggiungiHotel(self, nome, desc, citta, ind, numstanze):
        hotel = Hotel()
        hotel.nomehotel = nome
        hotel.deschotel = desc
        hotel.cittahotel = citta
        hotel.indhotel = ind
        hotel.numStanze = numstanze
        hotel.proprietario = self.cognome

    def aggiungiCamera(self, numero, posti, servizi, costo, hotel):
        stanza = Stanza()
        stanza.numStanza = numero
        stanza.postiletto = posti
        stanza.servizi = servizi
        stanza.costo = costo
        stanza.hotelDiAppartenenza = hotel.nomehotel
        hotel.numStanze += 1

class Cliente(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def effettuaPrenotazione(self, stanza, data):
        prenotazione = Prenotazione()
        prenotazione.cliente = self.email
        prenotazione.stanza = stanza.numStanza
        prenotazione.data = data


class Hotel(models.Model):
    nomehotel = models.CharField(max_length=30)
    deschotel = models.CharField(max_length=100)
    cittahotel = models.CharField(max_length=30)
    indhotel = models.CharField(max_length=30)
    numStanze = models.IntegerField()
    proprietario = models.CharField(max_length=30)


class Stanza(models.Model):
    numStanza = models.IntegerField()
    postiletto = models.IntegerField()
    servizi = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    hotelDiAppartenenza = models.CharField(max_length=30)


class Prenotazione(models.Model):
    idPrenotazione = models.IntegerField()
    hotel = Hotel
    cliente = models.CharField(max_length=30)
    stanza = models.IntegerField()
    data = models.DateTimeField()