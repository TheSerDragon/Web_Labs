from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=50, verbose_name="Название жанра")