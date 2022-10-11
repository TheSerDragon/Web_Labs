from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=100, verbose_name="Название игры")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена игры")
    platform = models.CharField(max_length=50, verbose_name="Платформа")
    language = models.BooleanField(verbose_name="Игра на русском языке?")