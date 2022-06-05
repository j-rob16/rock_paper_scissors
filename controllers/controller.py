from flask import redirect, render_template, request

from app import app
from models.game import Game
from models.player import Player
from models.players import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/versus/player')
def players_form():
    return render_template('versus_player/players_form.html', players=players)

@app.route('/versus/player', methods=['POST'])
def players_fight():
    print(request.form)
    name_1 = request.form['nameOne']
    weapon_1 = request.form['weaponOne']
    player_1 = Player(name_1, weapon_1)
    add_player(player_1)

    name_2 = request.form['nameTwo']
    weapon_2 = request.form['weaponTwo']
    player_2 = Player(name_2, weapon_2)
    add_player(player_2)

    play_game = Game(player_1, player_2)
    winner = play_game.play()
    return render_template('winner.html', winner=winner)


@app.route('/versus/computer')
def versus_computer_form():
    return render_template('versus_computer/computer_form.html', players=players)

@app.route('/versus/computer', methods=['POST'])
def computer_fight():
    name = request.form['name']
    weapon = request.form['weapon']
    player1 = Player(name, weapon)
    add_player(player1)
    player2 = add_adversary()
    add_player(player2)
    play_game = Game(player1, player2)
    winner = play_game.play()
    return render_template('winner.html', winner=winner)


@app.route('/<p_1_choice>/<p_2_choice>')
def player_vs_player(p_1_choice, p_2_choice):
    player_1 = Player('Player 1', str(p_1_choice))
    player_2 = Player('Player 2', str(p_2_choice))
    play_game = Game(player_1, player_2)
    winner = play_game.play()
    return render_template('winner.html', winner=winner)