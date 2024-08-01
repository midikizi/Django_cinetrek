from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import *

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'cinema', CinemaViewSet)
router.register(r'ville', VilleViewSet)
router.register(r'categorie', CategorieViewSet)
router.register(r'film', FilmViewSet)
router.register(r'place', PlaceViewSet)
router.register(r'salle', SalleViewSet)
router.register(r'projection', ProjectionViewSet)
# router.register(r'seance', SeanceViewSet)

router.register(r'cinemas', CinemaViewSet)
router.register(r'villes', VilleViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'films', FilmViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'salles', SalleViewSet)
router.register(r'seances', SeanceViewSet)
>>>> 1b03d19b5d0195e42e25cb7830cc5966d0f53179

"""
GET /cinema/ : Récupérer la liste de tous les cinémas.
POST /cinema/ : Créer un nouveau cinéma (en envoyant les données au format JSON).
GET /cinema/{id}/ : Récupérer les détails d'un cinéma spécifique.
PUT /cinema/{id}/ : Mettre à jour un cinéma existant.
DELETE /cinema/{id}/ : Supprimer un cinéma.
"""

urlpatterns = [
    path('', include(router.urls)),
]
