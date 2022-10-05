from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass