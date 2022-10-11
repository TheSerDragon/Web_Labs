from games.models import Game
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Game
        # Поля, которые мы сериализуем
        fields = ["pk", "game_name", "price", "platform", "language"]