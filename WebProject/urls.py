from django.contrib import admin
from django.urls import path

from WebProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GameList),
    path('game/<int:id>/', views.GetGame, name='game_url'),
]