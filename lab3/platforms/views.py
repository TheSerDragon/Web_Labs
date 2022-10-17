from rest_framework import viewsets
from platforms.serializers import PlatformSerializer
from platforms.models import Platform

class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Platform.objects.all().order_by('plat_name')
    serializer_class = PlatformSerializer  # Сериализатор для модели