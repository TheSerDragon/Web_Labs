from rest_framework import viewsets
from games.serializers import GameSerializer
from games.serializers import GenreSerializer
from games.serializers import PlatformSerializer
from games.serializers import PublisherSerializer
from games.models import Game
from games.models import Genre
from games.models import Platform
from games.models import Publisher

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Game.objects.all().order_by('price')
    serializer_class = GameSerializer  # Сериализатор для модели

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Genre.objects.all().order_by('genre_name')
    serializer_class = GenreSerializer  # Сериализатор для модели

class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Platform.objects.all().order_by('plat_name')
    serializer_class = PlatformSerializer  # Сериализатор для модели

class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Publisher.objects.all().order_by('year_found')
    serializer_class = PublisherSerializer  # Сериализатор для модели