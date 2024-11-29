from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='game') # (prefixe de l'url, classe gerant les requetes HTTP pour ces routes)

#  Routes générées automatiquement :

#     Liste des parties (GET) : /games/
#     Détail d'une partie (GET) : /games/<id>/
#     Créer une partie (POST) : /games/
#     Mettre à jour une partie (PUT) : /games/<id>/
#     Supprimer une partie (DELETE) : /games/<id>/

urlpatterns = [
    path('', include(router.urls)),  # Inclut les routes générées automatiquement dans l'application core
]
