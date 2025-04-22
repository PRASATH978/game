import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_values = {r: i+2 for i, r in enumerate(ranks)}  # 2 to 14

def draw_card():
    return random.choice(ranks) + random.choice(suits)

def get_rank_value(card):
    rank = card[:-1]
    return rank_values[rank]

def determine_winner(dragon, tiger):
    dragon_val = get_rank_value(dragon)
    tiger_val = get_rank_value(tiger)
    if dragon_val > tiger_val:
        return 'dragon'
    elif tiger_val > dragon_val:
        return 'tiger'
    else:
        return 'tie'
