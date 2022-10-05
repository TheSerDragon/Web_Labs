from django.db import models



# Create your models here.
class Game(models.Model):
    image = models.TextField(verbose_name='Изображение')
    name = models.CharField(max_length=100, verbose_name='Название')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    date = models.CharField(max_length=100, verbose_name='Дата')
    descrip = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = False
        db_table = 'games'
        verbose_name_plural = 'Игры'

class Developer(models.Model):
    id_dev = models.AutoField(primary_key=True)
    dev_image = models.CharField(max_length=512)
    dev_name = models.CharField(max_length=256)
    year_found = models.IntegerField()
    director = models.CharField(max_length=256)
    workers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'developer'

class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'genre'


class Platform(models.Model):
    id_plat = models.AutoField(primary_key=True)
    plat_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'platform'