from django.test import TestCase
from Booking.Booking.models import *


class ModelTest(TestCase):
    def testOggetti(self):
        albergatore1 = Albergatore(
            nome = "Piero",
            cognome = "Pieri",
            username="plazaPiero90",
            email = "plaza.hotel@gmail.com",
            password = "fgh34xZqw")

        cliente1 = Cliente(
            email = "gianni.tipo@gmail.com",
            password = "hJ45Cvbn2A")



