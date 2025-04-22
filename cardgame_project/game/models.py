from django.db import models
from django.contrib.auth.models import User
import random

class GameSession(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    dragon_card = models.CharField(max_length=5)
    tiger_card = models.CharField(max_length=5)
    result = models.CharField(max_length=10)
    bet_choice = models.CharField(max_length=10)  # dragon, tiger, tie
    is_win = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} - {self.result} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
