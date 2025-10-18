from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Platform
from .forms import GameForm

def home(request):
    return render(request, 'games/home.html')

def games_list(request):
    games = Game.objects.all()
    platform = Platform.objects.all()
    return render(request, 'games/games_list.html', {'games':games, 'platform':platform})

#CRUD
def create_game(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            game_form.save()
            return redirect('games_list')
    form = GameForm()
    return render(request, 'games/games_form.html', {'form':form})

def update_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_detail')
        form = GameForm(instance=game)
    return render(request, 'games/games_form.html', {'form':form})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'games/game_detail.html', {'game':game})

def detail_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        game.delete()
        return redirect('games_list')
    return render(request, 'games/game_delete_confirm.html', {'game':game})

