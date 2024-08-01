from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'cinemas', CinemaViewSet)
router.register(r'villes', VilleViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'films', FilmViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'salles', SalleViewSet)
router.register(r'seances', SeanceViewSet)

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
