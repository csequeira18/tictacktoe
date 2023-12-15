# Ultimate Tic Tac Toe Premise: 3 games must be played. Best of three wins. 
# Power-Ups will be rewarded to the winner of each round.
# x's = 1, o's = 2

class Player():
    def __init__(self, name):
        self.name = name
    def make_move(self, available_moves):
        # TODO: ask for move
        # TODO: if in available moves:
            pass

class PlayerUpgraded():
    def __init__(self, name, turn_count):
        super().__init__(name)
        #TODO: create powerups AFTER all game and player functions are done

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
    def availabe_moves(self):
         # TODO: assess board (if val = 0, or if val > 0)
         pass
    def show_board(self):
         # TODO: print out board
         pass
    def update_board(self):
         # TODO: after move, change correlating board value to either 1 or 2
         pass
    def check_win(self):
         # : check all possible combinations of winning
         pass
    def reset(self):
         self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
         # reset any other vals

if __name__ == "__main__":
    name1 = input("Enter player 1 name:" )
    name2 = input("Enter player 2 name:" )
    p1 = Player(name1)
    p2 = Player(name2)
    g = Game(p1, p2)
    g.play()


