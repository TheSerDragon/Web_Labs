from django.shortcuts import render
from rest_framework import viewsets
from games.serializers import GameSerializer
from games.models import Game
# Create your views here.

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Game.objects.all().order_by('price')
    serializer_class = GameSerializer  # Сериализатор для модели