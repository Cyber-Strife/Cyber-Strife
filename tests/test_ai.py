# test_ai.py

import unittest
from src.agents.ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):

    def setUp(self):
        self.agent = AIAgent("Test Overlord", 100, 50)

    def test_training(self):
        initial_hacking_power = self.agent.hacking_power
        self.agent.train(100)
        self.assertGreater(self.agent.hacking_power, initial_hacking_power)

    def test_battle(self):
        opponent = AIAgent("Opponent Overlord", 90, 60)
        result = self.agent.battle(opponent)
        self.assertEqual(result, "Test Overlord wins!")

    def test_get_status(self):
        status = self.agent.get_status()
        self.assertEqual(status["name"], "Test Overlord")
        self.assertEqual(status["hacking_power"], 100)
        self.assertEqual(status["defense"], 50)

if __name__ == '__main__':
    unittest.main()
