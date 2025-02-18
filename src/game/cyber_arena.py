# cyber_arena.py

from game_engine import GameEngine

class CyberArena(GameEngine):
    def __init__(self):
        super().__init__()

    def start_battle(self, player1, player2):
        match = self.create_match(player1, player2)
        return f"Battle started between {player1} and {player2}!"

    def conclude_battle(self, match, winner):
        self.end_match(match)
        return f"Match concluded. The winner is {winner}."
