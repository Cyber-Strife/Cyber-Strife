# simulate.py

import random
from src.agents.ai_agent import AIAgent

def simulate_battle(player1, player2):
    outcome = random.choice([player1, player2])
    print(f"Winner is: {outcome.name}")

def main():
    player1 = AIAgent("Player 1", 100, 50)
    player2 = AIAgent("Player 2", 90, 60)

    player1.train(100)
    player2.train(100)

    simulate_battle(player1, player2)

if __name__ == "__main__":
    main()
