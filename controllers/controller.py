from flask import redirect, render_template, request

from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/versus/player', methods=['post'])
def players_form():
    p1_name = request.form['p1_name']
    p1_weapon = request.form['p1_weapon']
    player_1 = Player(p1_name, p2_weapon)

    p2_name = request.form['p2_name']
    p2_weapon = request.form['p2_weapon']
    player_2 = Player(p2_name, p2_weapon)

    return redirect(f'/pvp/{player_1.choice}/{player_2.choice}')

@app.route('/pvp/<p_1_choice>/<p_2_choice>')
def player_vs_player(p_1_choice, p_2_choice):
    player_1 = Player('James', str(p_1_choice))
    player_2 = Player('Player_2', str(p_2_choice))
    play_game = Game(player_1, player_2)
    winner = play_game.play()
    return render_template('versus_player.html', winner=winner)