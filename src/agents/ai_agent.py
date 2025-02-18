# ai_agent.py

class AIAgent:
    def __init__(self, name, hacking_power, defense):
        self.name = name
        self.hacking_power = hacking_power
        self.defense = defense
        self.level = 1

    def train(self, experience_points):
        self.hacking_power += experience_points // 2
        self.defense += experience_points // 3
        self.level += 1

    def battle(self, opponent):
        if self.hacking_power > opponent.hacking_power:
            return f"{self.name} wins!"
        elif self.hacking_power < opponent.hacking_power:
            return f"{opponent.name} wins!"
        else:
            return "It's a tie!"

    def get_status(self):
        return {
            "name": self.name,
            "level": self.level,
            "hacking_power": self.hacking_power,
            "defense": self.defense
        }
