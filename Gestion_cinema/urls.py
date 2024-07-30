from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'cinemas', CinemaViewSet)
router.register(r'ville', VilleViewSet)
router.register(r'categorie', CategorieViewSet)
router.register(r'film', FilmViewSet)
router.register(r'place', PlaceViewSet)
router.register(r'salle', SalleViewSet)
router.register(r'projection', ProjectionViewSet)
router.register(r'seance', SeanceViewSet)

"""
GET /cinemas/ : Récupérer la liste de tous les cinémas.
POST /cinemas/ : Créer un nouveau cinéma (en envoyant les données au format JSON).
GET /cinemas/{id}/ : Récupérer les détails d'un cinéma spécifique.
PUT /cinemas/{id}/ : Mettre à jour un cinéma existant.
DELETE /cinemas/{id}/ : Supprimer un cinéma.
"""

urlpatterns = [
    path('', include(router.urls)),
]
