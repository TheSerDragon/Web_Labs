from games.models import Game
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Game
        # Поля, которые мы сериализуем
        fields = ["pk", "game_name", "genre", "publisher", "platform", "date_release", "description", "price"]