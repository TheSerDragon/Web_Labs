from rest_framework import viewsets
from genres.serializers import GenreSerializer
from genres.models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    serializer_class = GenreSerializer  # Сериализатор для модели