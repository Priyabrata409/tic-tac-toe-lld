from game import Game
from player import PlayerFactory

def main():
    player1 = PlayerFactory.create_player("Priyabrata", "X")
    player2 = PlayerFactory.create_player("Anuj", "0")
    game = Game([player1, player2])
    game.start_game()


main()