from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length=50, verbose_name="Название игры")
    genre = models.CharField(max_length=50, verbose_name="Жанр игры")
    publisher = models.CharField(max_length=50, verbose_name="Издатель игры")
    platform = models.CharField(max_length=50, verbose_name="Платформа для игры")
    date_release = models.CharField(max_length=50, verbose_name="Дата выхода")
    description = models.TextField(verbose_name="Описание игры")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена игры")

class Genre(models.Model):
    genre_name = models.CharField(max_length=50, verbose_name="Название жанра")

class Platform(models.Model):
    plat_name = models.CharField(max_length=50, verbose_name="Название платформы")

class Publisher(models.Model):
    pub_name = models.CharField(max_length=50, verbose_name="Название компании")
    year_found = models.IntegerField(verbose_name="Год основания")
    director = models.CharField(max_length=50, verbose_name="Глава компании")
    workers = models.IntegerField(verbose_name="Число сотрудников")

"""
class Genre(models.Model):
    id_genre = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(unique=True, max_length=64)

class Platform(models.Model):
    id_plat = models.BigAutoField(primary_key=True)
    plat_name = models.CharField(unique=True, max_length=64)

class Publisher(models.Model):
    id_pub = models.BigAutoField(primary_key=True)
    pub_name = models.CharField(unique=True, max_length=256)
    year_found = models.IntegerField(blank=True, null=True)
    director = models.CharField(unique=True, max_length=256)
    workers = models.IntegerField(blank=True, null=True)
    pub_image = models.CharField(max_length=512, default="/images/authors/author_icon.jpg")

class Game(models.Model):
    id_game = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=256)
    genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='genre', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='publisher', blank=True, null=True)
    platform = models.ForeignKey('Platform', models.DO_NOTHING, db_column='platform', blank=True, null=True)
    date_release = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default="0.00")
    game_image = models.CharField(max_length=512, default="images/mangas/manga_image.jpg")
"""