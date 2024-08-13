from Gestion_cinema.models import Place, Salle, Seance
from django.db import models

import uuid

# Create your models here.
class Ticket(models.Model):
    nomClient = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    codePayement = models.CharField(max_length=100, blank=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, default=None)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=None)
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE, default=None)

    def prix_total(self):
        return f"{self.prix + self.place.prix + self.seance.prix} F"

    def save(self, *args, **kwargs):
        if not self.codePayement:
            self.codePayement = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        code = str(uuid.uuid4()).replace('-', '_').upper()[:15]
        return code