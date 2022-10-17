from genres.models import Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Genre
        # Поля, которые мы сериализуем
        fields = ["pk", "genre_name"]