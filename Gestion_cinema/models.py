from django.db import models

# Create your models here.
class Ville(models.Model):
    nom = models.CharField(max_length=75)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField()
    cinema = models.ForeignKey()
    def __str__(self):
        return self.nom

class Cinema(models.Model):
    nom = models.CharField(max_length=75)
    nombreSalle = models.IntegerField(default=1)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField()
    ville = models.ManyToOneRel(Ville)
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Film(models.Model):
    titre = models.CharField(max_length=75)
    duree = models.FloatField()
    realisateur = models.CharField(max_length=75)
    description = models.TextField()
    photo = models.ImageField(upload_to="films/")
    dateSortie = models.DateField()
    category = models.ManyToOneRel(Categorie)
    def __str__(self):
        return self.titre

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    nombrePlace = models.IntegerField(default=1)
    cinema = models.ManyToOneRel(Cinema)
    def __str__(self):
        return self.nom

class Place(models.Model):
    numero = models.IntegerField()
    prix = models.FloatField()
    reservee = models.BooleanField(default=False)
    salle = models.ManyToOneRel(Salle)
    def __str__(self):
        return self.numero

class Projection(models.Model):
    date = models.DateField()
    prix = models.FloatField()
    film = models.OneToOneField(Film)
    class Meta:
        abstract = True

class Seance(Projection):
    heureDebut = models.DateTimeField()
    def __str__(self):
        return self.heureDebut

