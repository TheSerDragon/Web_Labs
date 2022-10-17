from django.db import models

class Platform(models.Model):
    plat_name = models.CharField(max_length=50, verbose_name="Название платформы")