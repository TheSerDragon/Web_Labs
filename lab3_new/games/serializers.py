from games.models import *
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Genre

        # Поля, которые мы сериализуем
        fields = ["id_genre", "genre_name"]

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Platform

        # Поля, которые мы сериализуем
        fields = ["id_plat", "plat_name"]

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Publisher

        # Поля, которые мы сериализуем
        fields = ["id_pub", "pub_name", "year_found", "director", "workers", "pub_image"]


class GameSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id_game", "game_name", "genre", "publisher", "platform", "date_release", "price", "description",
                  "game_image"]

class GameSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    publisher = PublisherSerializer()
    genre = GenreSerializer()

    class Meta:
        # Модель, которую мы сериализуем
        model = Game

        # Поля, которые мы сериализуем
        fields = ["id_game", "game_name", "genre", "publisher", "platform", "date_release", "price", "description",
                  "game_image"]

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "login", "password", "username", "address", "email"]


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ["id", "order_status_name", "order_status_description"]


# Остальные запросы к списку заказов
class POSTOrderSerializer(serializers.ModelSerializer):
    # order_statusid = OrderStatusSerializer()

    class Meta:
        model = Order
        fields = ["id", "userid", "order_statusid", "order_price_sum", "order_date"]


# for non-GET methods
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "order_id", "game_id"]



class GameInCartSerializer(serializers.ModelSerializer):
    game_id = GameSerializer()

    class Meta:
        model = Cart
        fields = ["game_id", "id", "order_id"]


# GET запросы к спику заказов
class GETOrderSerializer(serializers.ModelSerializer):
    order_statusid = OrderStatusSerializer()
    ordered_game = GameInCartSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "userid", "order_statusid", "order_price_sum", "order_date", "ordered_game"]