import random

from models.player import Player

players = []
weapons = ['rock', 'paper', 'scissors']

def add_player(player):
    players.append(player)

def add_adversary():
    choice = random.choice(weapons)
    print(choice)
    computer = Player('Computer', choice)
    return computer