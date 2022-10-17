from publishers.models import Publisher
from rest_framework import serializers

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Publisher
        # Поля, которые мы сериализуем
        fields = ["pk", "pub_name", "year_found", "director", "workers"]