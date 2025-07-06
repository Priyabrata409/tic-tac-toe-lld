from abc import ABC, abstractmethod
from board import Board

class MoveStrategy(ABC):
    @abstractmethod
    def get_move(self, board):
        pass


class HumanMoveStrategy(MoveStrategy):
    def get_move(self, board: Board):
        stop = False
        while not stop:
            row =  int(input("Please enter a row value (int) "))
            col =  int(input("Please enter a column value (int) "))
            if board.isAvailable(row, col):
                stop = True
                continue
            print("Oops place is already occupied")
        return row, col
        