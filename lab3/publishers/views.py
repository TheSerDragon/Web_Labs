from rest_framework import viewsets
from publishers.serializers import PublisherSerializer
from publishers.models import Publisher

class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Publisher.objects.all().order_by('year_found')
    serializer_class = PublisherSerializer  # Сериализатор для модели