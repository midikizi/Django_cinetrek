from django.db import models

# Create your models here.
class Cinema(models.Model):
    nom = models.CharField(max_length=75)
    nombreSalle = models.IntegerField(default=1)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField()

    def __str__(self):
        return self.nom

class Ville(models.Model):
    nom = models.CharField(max_length=75)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField()
    cinema = models.ManyToManyField(Cinema, verbose_name="")

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Film(models.Model):
    titre = models.CharField(max_length=75)
    duree = models.FloatField()
    realisateur = models.CharField(max_length=75)
    description = models.TextField()
    photo = models.ImageField(upload_to="films/")
    dateSortie = models.DateField()
    category = models.ManyToManyField(Categorie, verbose_name="")

    def __str__(self):
        return self.titre

class Place(models.Model):
    numero = models.IntegerField()
    prix = models.FloatField(default=0)
    reservee = models.BooleanField(default=False)
    libre = models.BooleanField(default=True)

    def __str__(self):
        return self.numero

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    nombrePlace = models.IntegerField(default=1)
    cinema = models.ForeignKey(Cinema, verbose_name="", on_delete=models.CASCADE)
    places = models.ManyToManyField(Place, verbose_name="")

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if self.nombrePlace >= len(self.places):
            super().save(*args, **kwargs)

    def prix_salle(self):
        prixSalle = 0
        prixSalle += [place.prix for place in self.places]
        return prixSalle

class Projection(models.Model):
    date = models.DateField()
    prix = models.FloatField(default=0)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    class Meta:
        abstract = True

    def __str__(self):
        return self.nom

class Seance(Projection):
    heureDebut = models.DateTimeField()

    def __str__(self):
        return self.heureDebut.strftime("%Y-%m-%d %H:%M")

