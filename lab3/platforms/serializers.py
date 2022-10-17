from platforms.models import Platform
from rest_framework import serializers

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Platform
        # Поля, которые мы сериализуем
        fields = ["pk", "plat_name"]