from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'game/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'game/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import login_required
from .models import GameSession
from .utils import draw_card, determine_winner

@login_required
def play_dragon_tiger(request):
    if request.method == "POST":
        bet = request.POST['bet']  # dragon, tiger, tie

        dragon_card = draw_card()
        tiger_card = draw_card()

        result = determine_winner(dragon_card, tiger_card)
        is_win = (result == bet)

        # Save to database
        GameSession.objects.create(
            player=request.user,
            dragon_card=dragon_card,
            tiger_card=tiger_card,
            result=result,
            bet_choice=bet,
            is_win=is_win
        )

        context = {
            'dragon_card': dragon_card,
            'tiger_card': tiger_card,
            'result': result,
            'bet': bet,
            'is_win': is_win
        }
        return render(request, 'game/dragon_tiger_result.html', context)

    return render(request, 'game/play_dragon_tiger.html')



def home(request):
    return render(request, 'game/home.html')

@login_required
def dashboard(request):
    return render(request, 'game/dashboard.html')

