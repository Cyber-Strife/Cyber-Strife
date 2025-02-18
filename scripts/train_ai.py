# train_ai.py

import time
from src.agents.ai_agent import AIAgent

def train_ai():
    agent = AIAgent("Training Overlord", 50, 30)
    for epoch in range(10):
        print(f"Training epoch {epoch + 1}")
        agent.train(100)
        time.sleep(1)

    print(f"Training completed! Final stats: {agent.get_status()}")

if __name__ == "__main__":
    train_ai()
