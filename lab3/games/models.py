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