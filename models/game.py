class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play(self):
        choice_1 = self.player_1.choice
        choice_2 = self.player_2.choice

        if choice_1 == choice_2:
            return None

        if choice_1 == 'rock':
            if choice_2 == 'paper':
                return self.player_2 
            if choice_2 == 'scissors':
                return self.player_1
            
        if choice_1 == 'paper':
            if choice_2 == 'scissors':
                return self.player_2
            if choice_2 == 'rock':
                return self.player_1
            
        if choice_1 == 'scissors':
            if choice_2 == 'rock':
                return self.player_2
            if choice_2 == 'paper':
                return self.player_1