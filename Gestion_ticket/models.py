from django.db import models

from Gestion_cinema.models import Place, Salle

# Create your models here.
class Ticket(models.Model):
    nomClient = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    codePayement = models.CharField(max_length=100)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    
    def prix_total(self):
        return self.prix + self.place.prix