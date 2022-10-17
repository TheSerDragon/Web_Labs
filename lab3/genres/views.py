from rest_framework import viewsets
from genres.serializers import GenreSerializer
from genres.models import Genre

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Genre.objects.all().order_by('genre_name')
    serializer_class = GenreSerializer  # Сериализатор для модели