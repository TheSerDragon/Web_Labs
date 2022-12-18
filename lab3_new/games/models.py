from django.db import models
from django.contrib.auth.models import PermissionsMixin

class Genre(models.Model):
    id_genre = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'genre'

class Platform(models.Model):
    id_plat = models.BigAutoField(primary_key=True)
    plat_name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'platform'

class Publisher(models.Model):
    id_pub = models.BigAutoField(primary_key=True)
    pub_name = models.CharField(unique=True, max_length=256)
    year_found = models.IntegerField(blank=True, null=True)
    director = models.CharField(unique=True, max_length=256)
    workers = models.IntegerField(blank=True, null=True)
    pub_image = models.CharField(max_length=512, default="images/publishers/")

    class Meta:
        managed = False
        db_table = 'publisher'

class Game(models.Model):
    id_game = models.BigAutoField(primary_key=True)
    game_image = models.CharField(max_length=512)
    game_name = models.CharField(max_length=256)
    genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='genre', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='publisher', blank=True, null=True)
    platform = models.ForeignKey('Platform', models.DO_NOTHING, db_column='platform', blank=True, null=True)
    date_release = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'game'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    address = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class OrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_status_name = models.CharField(max_length=128, blank=True, null=True)
    order_status_description = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status'


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    order_statusid = models.ForeignKey('OrderStatus', models.DO_NOTHING, db_column='order_statusID', default=6, blank=True, null=True)  # Field name made lowercase.
    order_price_sum = models.DecimalField(max_digits=7, decimal_places=2, default="0.00", blank=True, null=True)
    order_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'order'


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey('Order', models.DO_NOTHING, db_column='orderID', related_name="ordered_game", blank=True, null=True)  # Field name made lowercase.
    game_id = models.ForeignKey('Game', models.DO_NOTHING, db_column='gameID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'
