from rest_framework import viewsets, permissions
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-created_at')  # Liste des parties triées par date
    serializer_class = GameSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Les non-authentifiés peuvent lire, mais pas modifier
