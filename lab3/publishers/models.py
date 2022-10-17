from django.db import models

class Publisher(models.Model):
    pub_name = models.CharField(max_length=50, verbose_name="Название компании")
    year_found = models.IntegerField(verbose_name="Год основания")
    director = models.CharField(max_length=50, verbose_name="Глава компании")
    workers = models.IntegerField(verbose_name="Число сотрудников")