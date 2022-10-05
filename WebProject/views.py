from django.http import HttpResponse
from django.shortcuts import render
from datetime import date


from lab1.models import Game

def GameList(request):
    return render(request, 'games.html', {'data' : {
        'games': Game.objects.all()
    }})

def GetGame(request, id):
    return render(request, 'game.html', {'data' : {
        'game': Game.objects.filter(id=id)[0],
    }})