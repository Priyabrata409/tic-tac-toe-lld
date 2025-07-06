class Board:
    def __init__(self, board_size: int = 3):
        self.board = [["_"]* board_size for i in range(board_size)]
        self.total_values = board_size*board_size


    def isAvailable(self, row, col):
        return self.board[row][col] == "_"
    
    def isBoardFull(self):
        return self.total_values == 0
    
    def place_symbol(self, symbol: str, row: int, col: int):
        self.board[row][col] = symbol
        self.total_values-=1

    def hasPlayerWon(self, symbol):
        for row in self.board:
            if all(element == symbol for element in row):
                return True
        for i in range(len(self.board)):
            res = True
            for row in self.board:
                res *= (row[i] == symbol)
            if res:
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == symbol:
            return True
        return False


    def printBoard(self):
        for row in self.board:
            print(row)
            print("-----------")






    