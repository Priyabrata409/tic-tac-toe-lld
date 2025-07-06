from player import Player
from board import Board

class Game:
    def __init__(self, players: list[Player]):
        self.board = Board()
        self.players_queue = players

    
    def start_game(self):
        print("Welcone to tic-tac-toe Game!!!!!")
        while len(self.players_queue) > 1:
            player = self.players_queue.pop(0)
            stop = False
            if self.board.isBoardFull():
                print("Game Over no one wins!!!!")
            row, col = player.get_move(self.board)
            self.board.place_symbol(player.symbol, row, col)
            if self.board.hasPlayerWon(player.symbol):
                print(f"{player.name} has won the game")
                break
            self.board.printBoard()
            self.players_queue.append(player)
            

