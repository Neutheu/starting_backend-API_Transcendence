from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()  # Affiche le username du créateur car par defaut afficherait sa cle primaire comme son id par exemple
    players = serializers.StringRelatedField(many=True)  # Affiche les usernames des joueurs sous forme de liste

    # Les metadonnees
    class Meta:
        model = Game
        # liste des champs qui seront presents dans la reponse JSON
        fields = ['id', 'name']#, 'creator', 'players', 'status', 'created_at']#, 'updated_at']