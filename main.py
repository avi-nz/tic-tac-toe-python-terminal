"""Tic Tac Toe game in Python"""
import random

class Main:
    def __init__(self):
        self.board = ['-','-','-', 
                      '-','-','-', 
                      '-','-','-',]
        self.winner = None
        self.game_running = True
        self.single_player = False
        self.multiplayer = False
        self.turn = 0
        self.player = 'X'
        self.game_mode = ["single player", "multiplayer"]
        self.start_game()

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
    
    def spacer(self):
        print('\n')

    def check_horizontal_win(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != '-':
            self.game_running = False
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != '-':
            self.game_running = False
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != '-':
            self.game_running = False
            self.winner = self.board[6]
            return True

    def check_vertical_win(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != '-':
            self.game_running = False
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != '-':
            self.game_running = False
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != '-':
            self.game_running = False
            self.winner = self.board[2]
            return True

    def check_diagonal_win(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != '-':
            self.game_running = False
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != '-':
            self.game_running = False
            self.winner = self.board[2]
            return True
        
    def check_winner(self):
        if self.check_horizontal_win() or self.check_vertical_win() or self.check_diagonal_win():
            self.print_board()
            print(f"{self.winner} wins!")
            self.game_running = False

    def check_tie(self):
        if '-' not in self.board:
            print("It's a tie!")
            self.game_running = False
    
    def switch_player(self):
        if (self.turn % 2) == 0:
            self.player = "O"
            self.turn += 1
        else:
            self.player = "X"
            self.turn += 1

    def computer_move(self):
        self.switch_player()
        computer_decision = random.randint(0, 8)
        if self.board[computer_decision] == '-':
            self.board[computer_decision] = self.player
            self.switch_player()
        else:
            self.computer_move()


    def user_move(self):
        user_decision = int(input("Enter your move (1-9): "))
        if user_decision >= 1 and user_decision <= 9 and self.board[user_decision - 1] == '-':
            self.board[user_decision - 1] = self.player
            self.print_board()
            self.spacer()
            self.check_winner()
            self.check_tie()
        else:
            print("Invalid move")
            self.user_move()
    
    def game_mode_selection(self):
        for index, mode in enumerate(self.game_mode):
            print(f"{index + 1}. {mode}")
        self.game_mode_chosen = int(input("Select game mode: "))
        if self.game_mode_chosen == 1:
            self.single_player = True
        elif self.game_mode_chosen == 2:
            self.multiplayer = True
        else:
            print("Invalid selection")
            self.game_mode_selection()
    
    def start_game(self):
        self.game_mode_selection()
        while self.game_running:
            self.print_board()
            self.user_move()
            if self.game_running:
                if self.multiplayer:
                    self.switch_player()
                elif self.single_player:
                    self.computer_move()


if __name__ == "__main__":
    Main()
