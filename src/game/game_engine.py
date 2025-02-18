# game_engine.py

class GameEngine:
    def __init__(self):
        self.players = []
        self.matches = []

    def add_player(self, player):
        self.players.append(player)

    def create_match(self, player1, player2):
        match = {"player1": player1, "player2": player2, "status": "in_progress"}
        self.matches.append(match)
        return match

    def end_match(self, match):
        match["status"] = "completed"
        return match

    def get_match_results(self, match):
        if match["status"] == "completed":
            return f"Match between {match['player1']} and {match['player2']} is completed."
        else:
            return "Match is still in progress."
