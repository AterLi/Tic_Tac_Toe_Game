class GameBrain:
    def __init__(self, game_data):
        self.game_data = game_data
        self.display_board()

    def display_board(self):
        print("",
              self.game_data[1], "|", self.game_data[2], "|", self.game_data[3], "\n",
              self.game_data[4], "|", self.game_data[5], "|", self.game_data[6], "\n",
              self.game_data[7], "|", self.game_data[8], "|", self.game_data[9]
              )

    def input_signe(self, user_choose,  user_signe):
        self.game_data[user_choose] = user_signe

    def show_winner(self, last_move, player_nr):
        if (self.game_data[1] == self.game_data[2] == self.game_data[3]
                or self.game_data[4] == self.game_data[5] == self.game_data[6]
                or self.game_data[7] == self.game_data[8] == self.game_data[9]):
            print(f"We've got the winner with sign {last_move}, player nr {player_nr}")
            return False
        elif (self.game_data[1] == self.game_data[4] == self.game_data[7]
                or self.game_data[2] == self.game_data[5] == self.game_data[8]
                or self.game_data[3] == self.game_data[6] == self.game_data[9]):
            print(f"We've got the winner with sign {last_move}, player nr {player_nr}")
            return False
        elif (self.game_data[1] == self.game_data[5] == self.game_data[9] or
              self.game_data[8] == self.game_data[5] == self.game_data[3]):
            print(f"We've got the winner with sign {last_move}, player nr {player_nr}")
            return False
        else:
            return True

