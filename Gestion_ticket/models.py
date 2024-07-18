from django.db import models

from Gestion_cinema.models import Place, Salle


# Create your models here.
class Ticket(models.Model):
    nomClient = models.CharField(max_length=100)
    prix = models.IntegerField()
    codePayement = models.CharField(max_length=100)
    place = models.ForeignKey(Place)
    salle = models.ForeignKey(Salle)