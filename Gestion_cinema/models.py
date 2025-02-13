from django.db import models

# Create your models here.
class Ville(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    nom = models.CharField(max_length=75)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField(null=False)
    

    def __str__(self):
        return self.nom
    
class Cinema(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    nom = models.CharField(max_length=75)
    nombreSalle = models.IntegerField(default=1)
    longitude = models.FloatField()
    latitute = models.FloatField()
    altitude = models.FloatField(null=False)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    nom = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Film(models.Model):
    id = models.BigAutoField(primary_key=True)
    titre = models.CharField(max_length=75)
    duree = models.FloatField()
    realisateur = models.CharField(max_length=75)
    description = models.TextField()
    photo = models.ImageField(upload_to="films/",null=True, default='')
    dateSortie = models.DateField()
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titre

class Place(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    numero = models.IntegerField()
    prix = models.FloatField(default=0)
    reservee = models.BooleanField(default=False)
    libre = models.BooleanField(default=True)

    def __str__(self):
        return str(self.numero) 

class Salle(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    nom = models.CharField(max_length=100)
    nombrePlace = models.IntegerField(default=1)
    cinema = models.ForeignKey(Cinema, verbose_name="", on_delete=models.CASCADE)
    places = models.ForeignKey(Place, verbose_name="", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom


    # def save(self, *args, **kwargs):
    #     # Puis vérifiez la relation many-to-many
    #     if self.nombrePlace < len(self.places.all()):
    #         raise ValueError("Le nombre de places ne peut pas être inférieur au nombre de relations places.")
    #     else:
    #         super().save(*args, **kwargs)

    def prix_salle(self):
        prixSalle = 0
        prixSalle += [place.prix for place in self.places]
        return prixSalle

class Projection(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
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

