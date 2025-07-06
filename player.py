from abc import ABC
from move import MoveStrategy, HumanMoveStrategy
from board import Board

class Player(ABC):
    def __init__(self, name: str, symbol: str, move_strategy: MoveStrategy):
        self.name = name
        self.symbol = symbol
        self.move_strategy = move_strategy
    
    def get_move(self, board: Board):
        return self.move_strategy.get_move(board)


class HumanPlayer(Player):
    pass

class PlayerFactory:
    @staticmethod
    def create_player(name, symbol, player_type=None):
        return HumanPlayer(name, symbol, HumanMoveStrategy())


