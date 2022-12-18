from django.contrib import admin
from games import models

admin.site.register(models.Game)
admin.site.register(models.Platform)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)
admin.site.register(models.Users)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderStatus)