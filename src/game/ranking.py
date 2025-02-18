# ranking.py

class Ranking:
    def __init__(self):
        self.leaderboard = {}

    def update_ranking(self, player, score):
        self.leaderboard[player] = score

    def get_leaderboard(self):
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        return sorted_leaderboard

    def get_player_rank(self, player):
        rank = 1
        for p, score in self.get_leaderboard():
            if p == player:
                return rank
            rank += 1
        return None
