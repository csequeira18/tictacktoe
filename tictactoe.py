# Ultimate Tic Tack Toe Premise: 3 games must be played. Best of three wins. 
# Power-Ups will be rewarded to the winner of each round.

# TODO: create board
# create player
# create game
import numpy as np

BOARD_ROWS = 3
BOARD_COLS = 3

if __name__ == "__main__":
    name1 = input("Enter player 1 name:" )
    name2 = input("Enter player 2 name:" )
    p1 = Player(name1)
    p2 = Player(name2)
    g = Game(p1, p2)
    g.play()
        
class Player():
    def __init__(self, name):
        self.name = name
    def make_move(self, available_moves):
        print("{}'s turn".format(self.name))
        while True:
            try:
                row = int(input("Enter the row: "))
                col = int(input("Enter the col: "))
            except:
                continue
            action = (row, col)
            if action in available_moves:
                return action
class PlayerUpgraded():
    def __init__(self, name, turn_count):
        super().__init__(name)
        self.superPower = turn_count + 1
class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.gameover = False
        self.turn = 1
    def play(self):
        while not self.gameover


# board = {}

# def startGame():
#     print("Press enter to begin your game of Tic Tack Toe!")
#     print("\n")
#     print("Rules of the game: This games requires 2 players."
#           "Player 1 will mark the board with Xs and Player 2" 
#           "will mark the board with Os."
#           "Only one mark can be made by a player on their turn"
#           "To win, a player must mark three of their designated symbol on the board"
#           "in a row (vertically, horizontally, or diagonally).")
#     print("Player 1 will us Xs and Player 2 will use Os")
#     print("Rules: Player 1 and player 2, represented by X and O, take turns "
#           "marking the spaces in a 3*3 grid. The player who succeeds in placing "
#           "three of their marks in a horizontal, vertical, or diagonal row wins.")
#     print("\n")
#     input("Press enter to continue.")
#     print("\n")
# def board_full(board):
#     if board{0}:
#         return True
#     else:
#         return False

# def turn(playerNum, board):
#     if board_full(board) == False:
#         #proceed to take turn
#     print(board)

# def getWinner():
#     pass

# def main():
    
#     startGame()
#     #while loop: until board is full or winner:
#     turn()
#     getWinner


# if __name__ == "__main__":
#     main()






# # "Written by James Shah -- TO BE EDITED"
# # #Implementation of Two Player Tic-Tac-Toe game in Python.

# # ''' We will make the board using dictionary 
# #     in which keys will be the location(i.e : top-left,mid-right,etc.)
# #     and initialliy it's values will be empty space and then after every move 
# #     we will change the value according to player's choice of move. '''

# # theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
# #             '4': ' ' , '5': ' ' , '6': ' ' ,
# #             '1': ' ' , '2': ' ' , '3': ' ' }

# # board_keys = []

# # for key in theBoard:
# #     board_keys.append(key)

# # ''' We will have to print the updated board after every move in the game and 
# #     thus we will make a function in which we'll define the printBoard function
# #     so that we can easily print the board everytime by calling this function. '''

# # def printBoard(board):
# #     print(board['7'] + '|' + board['8'] + '|' + board['9'])
# #     print('-+-+-')
# #     print(board['4'] + '|' + board['5'] + '|' + board['6'])
# #     print('-+-+-')
# #     print(board['1'] + '|' + board['2'] + '|' + board['3'])

# # # Now we'll write the main function which has all the gameplay functionality.
# # def game():

# #     turn = 'X'
# #     count = 0


# #     for i in range(10):
# #         printBoard(theBoard)
# #         print("It's your turn," + turn + ".Move to which place?")

# #         move = input()        

# #         if theBoard[move] == ' ':
# #             theBoard[move] = turn
# #             count += 1
# #         else:
# #             print("That place is already filled.\nMove to which place?")
# #             continue

# #         # Now we will check if player X or O has won,for every move after 5 moves. 
# #         if count >= 5:
# #             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")                
# #                 break
# #             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break
# #             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break
# #             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break
# #             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break
# #             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break 
# #             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break
# #             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
# #                 printBoard(theBoard)
# #                 print("\nGame Over.\n")                
# #                 print(" **** " +turn + " won. ****")
# #                 break 

# #         # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
# #         if count == 9:
# #             print("\nGame Over.\n")                
# #             print("It's a Tie!!")

# #         # Now we have to change the player after every move.
# #         if turn =='X':
# #             turn = 'O'
# #         else:
# #             turn = 'X'        
    
# #     # Now we will ask if player wants to restart the game or not.
# #     restart = input("Do want to play Again?(y/n)")
# #     if restart == "y" or restart == "Y":  
# #         for key in board_keys:
# #             theBoard[key] = " "

# #         game()

# # if __name__ == "__main__":
# #     game()