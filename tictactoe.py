# Ultimate Tic Tac Toe Premise: 3 games must be played. Best of three wins. 
# Power-Ups will be rewarded to the winner of each round.
# x's = 1, o's = 2

class Player():
    def __init__(self, name):
        self.name = name
    def make_move(self, available_moves):
        print(self.name + "'s turn")
        # loop through moves until user enters valid move
        while True:
            # ask user for next move attempt
            row = int(input("Enter the row: "))
            col = int(input("Enter the col: "))
            move_attempt = (row, col)
            # if move attempt is valid, return next move
            if move_attempt in available_moves:
                return move_attempt

# class PlayerUpgraded():
#     def __init__(self, name, turn_tracker):
#         super().__init__(name)
#         # TODO: create powerups AFTER all game and player functions are done

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_wincount = 0
        self.player2_wincount = 0
        self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        self.turn_tracker = 1
        self.gameover = False
        self.game_count = 0
    def available_moves(self):
        empty_cells = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    empty_cells.append((row, col))

        return empty_cells

    def show_board(self):
         for i in range(3):
            line = "_____________"
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

    def update_board(self, move):
         # updates square with number of player who just played
         self.board[move[0]][move[1]] = self.turn_tracker
         # changes the turn determiner to the opposing player
         if self.turn_tracker == 1:
             self.turn_tracker = 2
         else:
             self.turn_tracker = 1

    def check_win(self):
    # Check rows
        for row in self.board:
            if all(cell == 1 for cell in row):
                self.gameover = True
                self.player1_wincount += 1
                return 1  # Player 1 (X) wins
            elif all(cell == 2 for cell in row):
                self.gameover = True
                self.player2_wincount += 1
                return 2  # Player 2 (O) wins

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == 1 for row in range(3)):
                self.gameover = True
                self.player1_wincount += 1
                return 1  # Player 1 (X) wins
            elif all(self.board[row][col] == 2 for row in range(3)):
                self.gameover = True
                self.player2_wincount += 1
                self.gameover = True

                return 2  # Player 2 (O) wins

        # Check diagonals
        if all(self.board[i][i] == 1 for i in range(3)) or all(self.board[i][2 - i] == 1 for i in range(3)):
            self.gameover = True
            self.player1_wincount += 1
            return 1  # Player 1 (X) wins
        elif all(self.board[i][i] == 2 for i in range(3)) or all(self.board[i][2 - i] == 2 for i in range(3)):
            self.gameover = True
            self.player2_wincount += 1
            return 2  # Player 2 (O) wins

        # Check for a tie
        if all(cell != 0 for row in self.board for cell in row):
            self.gameover = True
            return 3  # Tie

        # No winner yet
        return 0
    
    def determine_trio_winner(self):
        if self.game_count == 3:
            if self.player1_wincount > self.player2_wincount:
                return self.player1.name
            elif self.player1_wincount < self.player2_wincount:
                return self.player2.name
            else:
                return "neither player"
            
    def reset(self):
        # reset board
         self.board = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        # reset turn count
         self.turn_tracker = 1
        # resets gameover determinator
         self.gameover = False
        # keep track of game count
         if self.game_count <= 3:
             self.game_count += 1
         else:
             self.player1_wincount = 0
             self.player2_wincount = 0

    def play(self):
         # ask players to make moves until game board determines game over
         while not self.gameover:
            self.show_board()
            moves = self.available_moves()
            p1_turn = self.player1.make_move(moves)
            self.update_board(p1_turn)
            self.show_board()
            winner = self.check_win()
            if self.gameover:
                if winner == 1:
                    print(str(self.player1.name) + " wins!")
                elif winner == 2:
                    print(str(self.player2.name) + " wins!")
                else:
                    print("Tie!")
                self.reset()
                break
            else:
                self.show_board()
                moves = self.available_moves()
                p2_turn = self.player2.make_move(moves)
                self.update_board(p2_turn)
                self.show_board()
                winner = self.check_win()
                if self.gameover:
                    if winner == 1:
                        print(str(self.player1.name) + " wins!")
                    elif winner == 2:
                        print(str(self.player2.name) + " wins!")
                    else:
                        print("Tie!")
                    self.reset()
                    break
        
         if self.game_count < 3:
            self.play()
         if self.game_count == 3:
            print("Congratulations " + str(self.determine_trio_winner()) + " on winning the best of three games!")

if __name__ == "__main__":
    name1 = input("Enter player 1 name: " )
    name2 = input("Enter player 2 name: " )
    player1 = Player(name1)
    player2 = Player(name2)
    game = Game(player1, player2)
    game.play()


