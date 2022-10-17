from games.models import Game
from games.models import Genre
from games.models import Platform
from games.models import Publisher
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Game

        # Поля, которые мы сериализуем
        fields = ["pk", "game_name", "genre", "publisher", "platform", "date_release", "description", "price"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Genre

        # Поля, которые мы сериализуем
        fields = ["pk", "genre_name"]

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Platform

        # Поля, которые мы сериализуем
        fields = ["pk", "plat_name"]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Publisher

        # Поля, которые мы сериализуем
        fields = ["pk", "pub_name", "year_found", "director", "workers"]