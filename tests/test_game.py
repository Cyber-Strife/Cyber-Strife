# test_game.py

import unittest
from src.game.game_engine import GameEngine
from src.agents.ai_agent import AIAgent

class TestGameEngine(unittest.TestCase):

    def setUp(self):
        self.engine = GameEngine()
        self.player1 = AIAgent("Player 1", 100, 50)
        self.player2 = AIAgent("Player 2", 90, 60)

    def test_create_match(self):
        match = self.engine.create_match(self.player1, self.player2)
        self.assertEqual(match["status"], "in_progress")

    def test_end_match(self):
        match = self.engine.create_match(self.player1, self.player2)
        ended_match = self.engine.end_match(match)
        self.assertEqual(ended_match["status"], "completed")

if __name__ == '__main__':
    unittest.main()
