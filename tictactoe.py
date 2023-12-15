# Ultimate Tic Tac Toe Premise: 3 games must be played. Best of three wins. 
# Power-Ups will be rewarded to the winner of each round.
# x's = 1, o's = 2

class Player():
    def __init__(self, name):
        self.name = name
    def make_move(self, available_moves):
        print(self.name + "'s turn")
        # TODO: if in available moves:
        pass

class PlayerUpgraded():
    def __init__(self, name, turn_count):
        super().__init__(name)
        # TODO: create powerups AFTER all game and player functions are done

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        self.turncount = 1
        self.gameover = False
    def availabe_moves(self):
         # TODO: assess board (if val = 0, or if val > 0)
         pass
    def show_board(self):
         for i in range(3):
            line = "_______________"
            print(line)
            row = "|"
            for j in range(3):
                if self.board[i][j] == 0:
                     row += "  "
                elif self.board[i][j] == 1:
                     row += " X"
                elif self.board[i][j] == 2:
                     row += " O"
                row += " |"
            print(row)
         print(line)
    def update_board(self):
         # TODO: after move, change correlating board value to either 1 or 2
         pass
    def check_win(self):
         # TODO: check all possible combinations of winning
         # return 0 if no winner
         # return 1 if player 1 (X) wins
         # return 2 if player 2 (O) wins
         # return 3 if tie
         pass
    def reset(self):
         self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
         self.turncount = 1
         self.gameover = False
    def play(self):
         self.show_board()
         #self.player
         while self.gameover == False:
            if self.gameover:
                if self.check_win() == 1:
                    print(self.player1.name() + " wins!")
                elif self.check_win() == 2:
                    print(self.player2.name() + " wins!")
                else:
                    print("Tie!")
            else:
                if self.check_win() > 0:
                    self.gameover = True

if __name__ == "__main__":
    name1 = input("Enter player 1 name:" )
    name2 = input("Enter player 2 name:" )
    p1 = Player(name1)
    p2 = Player(name2)
    g = Game(p1, p2)
    g.play()


